# 在相邻场景中独立重建 if + raise 校验结构

用户在不查看前两个 `raise` 示例文件的要求下，根据自然语言说明独立写出一个完整可运行的 Python 程序：创建 `age = -1`，用 `if age < 0:` 控制是否进入异常分支，在缩进块中执行 `raise ValueError("age cannot be below zero")`，并在分支之后放置 `print("accepted")`。用户在运行前正确预测会抛出异常且不会打印 `accepted`，运行结果与 traceback 一致；也能正确预测把 `age` 改成正数后会跳过 `raise` 并继续打印。

随后经一次最小职责确认，用户能够明确区分：`if` 只决定是否执行到异常分支，`raise` 语句本身才真正创建并抛出 `ValueError`。

这构成了对 `if` + `raise ValueError(...)` 控制流的一次相邻迁移与独立重建证据。它不证明已经掌握 `try` / `except`、异常恢复、函数值传递、bounded retry，或延迟后的保留能力。
