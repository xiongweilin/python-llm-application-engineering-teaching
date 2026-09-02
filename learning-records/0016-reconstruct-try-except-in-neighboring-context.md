# 在相邻场景中独立重建 try / except 控制流

用户在不查看前两个 `try` / `except` 示例文件的要求下，根据自然语言说明独立写出一个完整可运行的 Python 程序：在 `try` 块中执行 `raise ValueError("invalid price")`，用匹配的 `except ValueError:` 处理该异常并打印 `price handled`，随后在整个 `try` / `except` 结构之后打印 `finished`。

用户在运行前正确预测完整输出为 `price handled`、`finished`，正确预测不会出现 traceback，实际运行结果一致。用户能够明确说明：`ValueError` 确实由 `raise` 语句产生；`except ValueError:` 因异常类型匹配而执行并处理该异常；异常被处理后不会沿未处理异常路径产生 traceback；后续 `finished` 既位于 `try` / `except` 结构之外，又因为前面的异常已经被处理而在运行时可达。

此前出现过把“没有 traceback”压缩成“没有异常发生”的误区。经过 §2 条件性 `Distinction judgment` 对 raised/unhandled、raised/handled、never-raised 三种路径的区分，以及一次受控 never-raised 对照后，本次相邻独立重建中该区分保持正确。

这构成了对基础 `try` / `except ValueError:` 控制流的一次相邻迁移与独立重建证据。它不证明已经掌握多异常分支、`else` / `finally`、重新抛出异常、异常对象绑定、嵌套异常处理、函数值传递、callback boundary、bounded retry，或延迟后的保留能力。
