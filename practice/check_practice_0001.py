r"""零依赖检查器：python .\check_practice_0001.py"""

from __future__ import annotations

from collections.abc import Callable
from types import ModuleType

Check = tuple[str, Callable[[], bool], str]


def run_checks(answers: ModuleType | object) -> int:
    class FlakyAction:
        def __init__(self, failures: int) -> None:
            self.failures = failures
            self.calls = 0

        def __call__(self) -> str:
            self.calls += 1
            if self.calls <= self.failures:
                raise RuntimeError("暂时失败")
            return "完成"

    def check_states() -> bool:
        expected = [
            ("waiting", "start", "running"),
            ("running", "finish", "done"),
            ("running", "fail", "failed"),
        ]
        if any(answers.next_state(state, event) != result for state, event, result in expected):
            return False
        try:
            answers.next_state("waiting", "finish")
        except ValueError:
            return True
        return False

    def check_retry() -> bool:
        action = FlakyAction(failures=2)
        if answers.retry(action, 3) != "完成" or action.calls != 3:
            return False

        exhausted = FlakyAction(failures=5)
        try:
            answers.retry(exhausted, 2)
        except RuntimeError:
            if exhausted.calls != 2:
                return False
        else:
            return False

        try:
            answers.retry(lambda: "不应执行", 0)
        except ValueError:
            return True
        return False

    def check_idempotency() -> bool:
        store: dict[str, object] = {}
        first_payload = {"value": 1}
        first_call = answers.create_once(store, "op-1", first_payload)
        if not isinstance(first_call, tuple) or len(first_call) != 2:
            return False
        first_result, first_reused = first_call
        if first_result is not first_payload or first_reused is not False:
            return False
        if store != {"op-1": first_payload}:
            return False

        second_payload = {"value": 999}
        second_call = answers.create_once(store, "op-1", second_payload)
        if not isinstance(second_call, tuple) or len(second_call) != 2:
            return False
        second_result, second_reused = second_call
        if second_result is not first_payload or second_reused is not True:
            return False
        if store != {"op-1": first_payload}:
            return False

        try:
            answers.create_once(store, "", {"value": 2})
        except ValueError:
            return True
        return False

    def check_batch() -> bool:
        def handler(item: int) -> int:
            if item < 0:
                raise ValueError("不能为负数")
            if item == 99:
                raise RuntimeError("系统故障")
            return item * 2

        result = answers.process_batch([2, -1, 3], handler)
        if result != {
            "results": [4, 6],
            "errors": [{"position": 2, "error": "不能为负数"}],
        }:
            return False

        try:
            answers.process_batch([1, 99, 2], handler)
        except RuntimeError:
            return True
        return False

    checks: list[Check] = [
        (
            "第1题 normalize_name",
            lambda: answers.normalize_name("  Alice  ") == "alice"
            and answers.normalize_name("小 林") == "小 林",
            "稳定结构：只做确定性转换；Python 模型：正确使用 str 对象的方法",
        ),
        (
            "第2题 validate_order",
            lambda: answers.validate_order(10, 2) == []
            and answers.validate_order(0, 2) == ["价格必须大于0"]
            and answers.validate_order(0, -1)
            == ["价格必须大于0", "数量必须大于0"],
            "稳定结构：执行两条独立规则；Python 模型：用可变 list 累计状态",
        ),
        (
            "第3题 next_state",
            check_states,
            "稳定结构：只允许显式状态转换；Python 模型：用 tuple 作为 dict 复合键",
        ),
        (
            "第4题 retry",
            check_retry,
            "稳定结构：有限尝试并传播最终失败；Python 模型：函数对象与异常控制流",
        ),
        (
            "第5题 create_once",
            check_idempotency,
            "稳定结构：同一操作只产生一次写入；Python 模型：修改 dict 并返回二元组",
        ),
        (
            "第6题 process_batch",
            check_batch,
            "稳定结构：隔离输入错误但传播系统故障；Python 模型：函数对象与异常类型匹配",
        ),
    ]

    failures = 0
    for title, check, hint in checks:
        try:
            passed = check()
        except Exception as exc:  # 把练习失败转换成可读反馈
            failures += 1
            print(f"✗ {title}：运行时出现 {type(exc).__name__}: {exc}")
            continue

        if passed:
            print(f"✓ {title}")
        else:
            failures += 1
            print(f"✗ {title}：{hint}")

    if failures:
        print(f"\n还有 {failures} 题没有通过。可以把代码或输出发给 Codex。")
    else:
        print("\n六题都通过了。下一步请解释前两层，再由 Codex检查第三层接口细节。")
    return failures


if __name__ == "__main__":
    import practice_0001_answers

    raise SystemExit(1 if run_checks(practice_0001_answers) else 0)
