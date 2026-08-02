"""Python 动手练习场：语法快速恢复与工程化第一组。

把每个函数中的 pass 换成自己的代码。
暂时不要追求最短写法，先让代码表达清楚。
"""


def normalize_name(name: str) -> str:
    """第1题：去掉两端空白并转成小写。"""
    pass


def validate_order(price: int, quantity: int) -> list[str]:
    """第2题：返回价格和数量的确定性校验错误。"""
    pass


def next_state(current: str, event: str) -> str:
    """第3题：根据当前状态和事件执行有限状态转换。"""
    pass


def retry(action, max_attempts: int):
    """第4题：有限重试 action，成功立即返回，耗尽后重新抛出异常。"""
    pass


def create_once(
    store: dict[str, object], operation_key: str, payload: object
) -> tuple[object, bool]:
    """第5题：同一操作只创建一次，返回（结果，是否复用）。"""
    pass


def process_batch(items: list[int], handler) -> dict[str, object]:
    """第6题：逐项调用 handler，隔离 ValueError 并保留其他异常。"""
    pass


if __name__ == "__main__":
    print("可以先运行检查器，也可以在这里临时打印函数结果。")
