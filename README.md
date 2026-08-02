# Python、数学、LLM、RAG 与 Agent 工程

这是唯一活动课程。Windows 开始菜单入口为 **Python 与 LLM 应用工程**；它会静默启动本地课程服务器并打开首页。

## 现在怎样继续

1. 打开开始菜单中的课程入口。
2. 打开正式学习会话 2“重试、防重复与批处理”。
3. 依次完成三个不同问题；每个问题都完整经过定向、底层逻辑、Python 细节、预测、核心实现、迁移和小结七步，页面每次只显示一个步骤。
4. 三个问题共九项任务全部完成后，在汇总页复制完整证据，只与老师互动一次。

第 1–2 题已经形成的学习证据保留。A/B/C 原型已退出活动入口；正式会话采用 A 的单步骨架，并加入详细的抽象逻辑与具体编程解释。

需要复习时，从首页进入“综合复习已有能力”。它把环 0 的 10 条基线记录连接成一个完整会话，不要求逐页重做旧题，也不改变当前正式会话进度。正式会话 1 新形成的状态转换记录单独保留。

## 课程怎样组织

- `FINAL-CAPABILITY-CONTRACT.md`：完整课程唯一最终能力事实来源。
- `index.html`：唯一首页与当前下一步。
- `lessons/`：正式会话、综合复习会话、已完成复习页和候选材料；页面必须显式标明身份，只有正式会话承担当前进度。
- `practice/`：可运行的 Python 小练习和紧反馈。
- `lessons/0010-state-and-permitted-actions.html`：已完成的正式学习会话 1。
- `lessons/0011-integrated-review-established-capabilities.html`：10 条已有能力的单一综合复习入口。
- `lessons/0012-failure-retry-stop.html`：当前正式学习会话 2。
- 会话 3“模块、诊断与授权边界”尚未生成正式页；届时先做无答案间隔回忆，再学习模块责任、测试诊断和授权边界三个问题。
- `practice/prototype-guided-session.html`：已完成选择的设计原型，不承担当前进度。
- `reference/`：完整四阶段十七环路线、最终能力契约、跨会话总术语和有明确归属的参考卡。
- `learning-records/`：已经由表现证明的能力，不是学习日志。
- `runtime/`：静默启停和自动验证脚本。

每个正式会话和综合复习会话页面下方都有“本会话中文术语”；总术语表只用于跨会话复习。浏览器中的页面规范见 [学习会话页面规范](reference/0004-session-page-contract.html)，规范源文件为 [SESSION-PAGE-CONTRACT.md](SESSION-PAGE-CONTRACT.md)。

完整设计见 [TEACHING-OVERVIEW.md](TEACHING-OVERVIEW.md)。课程采用项目与理论双向螺旋：真实任务可以提前触发数学或模型知识，但数学、物理、Transformer、训练数值、多主体和可靠性都有独立关口，不会因项目暂时没用到而删除。
