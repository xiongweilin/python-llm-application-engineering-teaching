# Python、数学、LLM、RAG 与 Agent 工程

这是唯一活动课程。Windows 开始菜单入口为 **Python 与 LLM 应用工程**；它会静默启动本地课程服务器并打开首页。

## 现在怎样继续

1. 打开开始菜单中的课程入口。
2. 打开正式学习会话 2“重试、防重复与批处理”。
3. 依次完成三个不同问题；每个问题都完整经过定向、底层逻辑、Python 细节、预测、核心实现、迁移和小结七步，页面每次只显示一个步骤。
4. 三个问题共九项任务全部完成后，在汇总页复制完整证据，只与老师互动一次。

第 1–2 题已经形成的学习证据保留。A/B/C 原型已退出活动入口；正式会话采用 A 的单步骨架，并加入详细的抽象逻辑与具体编程解释。

若仓库位置发生变化，运行 `pwsh -NoProfile -NonInteractive -File .\runtime\install-start-menu-shortcut.ps1` 可幂等创建或更新开始菜单入口。替换旧入口前，脚本会在本地课程状态目录中保留回滚备份。

需要复习时，从首页进入“综合复习已有能力”。它把环 0 的 10 条基线记录连接成一个完整会话，不要求逐页重做旧题，也不改变当前正式会话进度。正式会话 1 新形成的状态转换记录单独保留。

## 课程怎样组织

活动文档保持最小且充分：每类事实只保留一个拥有者，历史演变由 Git 和 ADR 保存，不再维护同义总览或 HTML 副本。

- `FINAL-CAPABILITY-CONTRACT.md`：完整课程唯一最终能力事实来源，包含主线、研究扩展和最终综合项目要求。
- `index.html`：唯一首页与当前下一步。
- `lessons/`：正式会话、综合复习会话、已完成复习页和候选材料；页面必须显式标明身份，只有正式会话承担当前进度。
- `practice/`：可运行的 Python 小练习和紧反馈。
- `lessons/0010-state-and-permitted-actions.html`：已完成的正式学习会话 1。
- `lessons/0011-integrated-review-established-capabilities.html`：10 条已有能力的单一综合复习入口。
- `lessons/0012-failure-retry-stop.html`：当前正式学习会话 2。
- 会话 3“模块、诊断与授权边界”尚未生成正式页；届时先做无答案间隔回忆，再学习模块责任、测试诊断和授权边界三个问题。
- `practice/prototype-guided-session.html`：已完成选择的设计原型，不承担当前进度。
- `reference/0002-course-progress.html`：四阶段十七环、环级责任、关口及最终能力—关口覆盖索引的唯一事实来源。
- `SESSION-PAGE-CONTRACT.md`：正式会话页面结构的唯一规范。
- `NOTES.md`：当前教学状态、用户偏好和课程生成约束；不重新定义最终能力或环级路线。
- `RESOURCES.md`：来源入口与使用边界。
- `docs/decisions/`：只记录课程架构为什么这样修改；不替代能力契约或环级路线。
- `reference/`：完整路线、跨会话总术语和有明确归属的参考卡。
- `learning-records/`：已经由表现证明的能力，不是学习日志。
- `runtime/`：静默启停和自动验证脚本。

每个正式会话和综合复习会话页面下方都有“本会话中文术语”；总术语表只用于跨会话复习。页面规范直接见 [SESSION-PAGE-CONTRACT.md](SESSION-PAGE-CONTRACT.md)，不再维护内容相同的 HTML 副本。

课程采用项目与理论双向螺旋，并以有限表示、有限维、可计算模型为数学主线：环 5 形成信念，环 7 完成单步选择，环 8 完成跨时间选择，环 9 分析多主体规则，环 14 接入权限与人工容量，环 15 验证真实效果。完整环级设计见[课程路线](reference/0002-course-progress.html)，毕业要求见[最终能力契约](FINAL-CAPABILITY-CONTRACT.md)，采用这一结构的原因见[架构决策](docs/decisions/0001-finite-computable-curriculum-core.md)。数学物理与一般化理论保留为研究扩展，不再作为主线毕业关口。
