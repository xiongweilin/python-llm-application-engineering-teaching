# Python、数学、LLM、RAG 与 Agent 工程 Resources

## Knowledge

- Local: `\\wsl.localhost\Ubuntu-22.04\srv\stack\catalog-ops-automation`
  Catalog 当前源码、测试、配置和 ADR。用于验证真实模块、调用链、状态、并发、幂等、RPA 和 Odoo 行为。
- Local: `D:\download\ratio\商品上架自动化项目\TEACHING-GUIDE.md`
  Catalog 的架构、模块和关键节点导览。用于选择阅读入口；具体事实仍回到当前源码和测试核验。
- Local: `D:\download\ratio\商品上架自动化项目\README.md`
  当前运行边界、验证入口与真实回放说明。涉及运行时行为时先核对项目当前状态。
- Local: `\\wsl.localhost\Ubuntu-22.04\srv\stack\feedback-analysis-agent`
  Feedback 当前源码、测试、配置和 ADR。用于验证会话、隐私、证据、裁决、恢复、聚类、评测与候选晋级。
- Local: `D:\download\ratio\客户反馈项目\TEACHING-GUIDE.md`
  Feedback 的架构、数据流、模块和关键节点导览。用于建立学习顺序，不替代源码证据。
- Local: `D:\download\ratio\客户反馈项目\README.md`
  项目定位、当前证据、数据边界和验证入口。
- Local: `D:\download\ratio\领域模型\计算机领域模型.md`
  用于区分程序、状态、控制流、数据流、接口、并发、持久化、反馈和运行证据。
- Local: `D:\download\ratio\领域模型\教育领域模型.md`
  用于安排激活、分化、连接、稳定、迁移、提示退出和能力证据；课程不能用教学活动替代学习。
- Local: `D:\download\ratio\领域模型\数学领域模型.md`
  用于数量、近似、概率、向量、优化和证据边界；具体算法仍需教材、代码与实验支持。
- Local: `D:\download\ratio\领域模型\组织制度领域模型.md`
  用于理解分工、接口、授权、规则、问责、候选晋级和退出，不把技术执行能力误作决定权。
- Local: `D:\download\ratio\有限宇宙\跨领域共同结构.md`
  用于识别状态—转移、顺序—依赖、反馈、瓶颈、尺度和路径依赖；类比只产生候选，不证明机制相同。
- Local: `D:\download\ratio\有限宇宙\有限变化实践.md`
  用于把改动组织为目的、权限、方案、执行、验证、恢复和退出的循环，并随副作用风险提高程序强度。
- Local: `D:\download\ratio\有限宇宙\有限智能.md`
  用于区分结构传承、直接经验、可调用能力与情境校正。
- Local: `D:\download\ratio\有限宇宙\证据与演化语义.md`
  候选规范，仅用于区分材料、观察、陈述、决定、修订和结果，以及版本变化后的重新验证；不得视为项目正式契约。
- [Python Tutorial](https://docs.python.org/zh-cn/3/tutorial/)
  Python 官方中文教程。用于控制流、函数、数据结构、模块、异常、类和迭代器。
- [Python Standard Library](https://docs.python.org/zh-cn/3/library/)
  官方标准库。用于 `csv`、`decimal`、`re`、`hashlib`、`unicodedata`、HTTP 与 XML-RPC。
- [pytest Documentation](https://docs.pytest.org/en/stable/)
  用于 fixture、参数化、异常断言和失败定位。
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
  用于 HTTP 路由、依赖、请求验证和生命周期。
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
  用于输入输出契约、枚举、验证和序列化。
- [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
  用于 ORM、Session、查询、事务和关系。
- [PostgreSQL SELECT](https://www.postgresql.org/docs/current/sql-select.html)
  用于行锁、`FOR UPDATE` 与 `SKIP LOCKED` 的当前官方语义。
- [OpenStax Statistics](https://openstax.org/books/statistics/pages/8-introduction)
  用于抽样、估计、方差、置信区间和结论强度；进入阶段 B · 环 5 时配合小数据实验，不把公式复述当作统计判断。
- [MIT OpenCourseWare: Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)
  用于导数、积分、局部近似、优化与微分方程入口；问题集和解答用于阶段 B 的计算证据。
- [MIT OpenCourseWare: Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/)
  用于偏导、梯度、链式法则、向量场、线积分、散度和旋度。
- [MIT OpenCourseWare: Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/)
  用于基、投影、特征值、秩、最小二乘和 SVD 的理论、计算与问题集。
- [MIT OpenCourseWare: Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/)
  用于状态空间、线性系统、相图、稳定性、模态与局部线性化。
- [MIT OpenCourseWare: Vibrations and Waves](https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/pages/syllabus/)
  用于振子、能量、耦合系统、正常模态、边界条件、波与傅里叶分解；物理结论必须由方程或实验核验。
- [Open Yale Courses: Game Theory](https://oyc.yale.edu/economics/econ-159)
  用于策略、最佳反应、均衡、承诺、可信度与信息边界；后续再用项目中的权限、激励和退出情境迁移。
- [PyTorch tensor tutorial](https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html)
  用于 shape、axis、张量运算和 autograd 入门。
- [PyTorch broadcasting semantics](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)
  用于判断广播表达式为何成立或失败。
- [PyTorch autograd tutorial](https://docs.pytorch.org/tutorials/beginner/basics/autograd_tutorial.html)
  用于计算图、链式法则、反向传播、梯度累积和 Jacobian 乘积的可运行核验。
- [PyTorch optimizers](https://docs.pytorch.org/docs/stable/optim)
  用于 SGD、动量、Adam 与优化器状态；具体行为进入相应会话时再以当前版本核验。
- [PyTorch numerical accuracy](https://docs.pytorch.org/docs/stable/notes/numerical_accuracy.html)
  用于浮点有限精度、非结合性、极值、NaN/Inf、病态矩阵和不同批量计算的数值差异。
- [PyTorch Automatic Mixed Precision](https://docs.pytorch.org/docs/stable/accelerator/amp.html)
  用于 FP16/BF16、autocast、梯度缩放和精度—性能权衡。
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
  注意力与 Transformer 的原始论文入口；进入模型机制支线时使用。
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html)
  RAG 的原始论文入口，用于区分参数记忆、检索和生成。
- [LoRA](https://arxiv.org/abs/2106.09685)
  低秩适配原始论文；仅在评估表明需要微调时进入。
- [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/)
  检索、评分和评价指标的教材入口。
- [OpenAI Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
  当前结构化输出接口实例；使用前核验当前字段和限制。
- [OpenAI Using tools](https://developers.openai.com/api/docs/guides/tools)
  当前工具调用实例；用于候选调用与执行边界，不作为永久接口记忆。
- [OpenAI Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
  用于任务定义、测试集和反馈循环。
- [Test-Enhanced Learning](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
  检索练习研究入口，用于先回忆、后反馈的设计。
- [Distributed practice in verbal recall tasks](https://doi.org/10.1037/0033-2909.132.3.354)
  分散练习综述入口，用于隔开若干单元后的再次提取。

## Wisdom (Communities)

- Local: 两个项目的 `tests/`、运行回放、ADR 和真实故障记录
  用于判断本项目什么算正确、哪些边界曾失败，以及修改是否能够恢复。
- [Python Discussions](https://discuss.python.org/)
  Python 官方社区，用于语言、标准库和打包行为争议。
- [PyTorch Forums](https://discuss.pytorch.org/)
  用于 shape、数值、性能和实现问题的实践反馈。
- [Hugging Face Forums](https://discuss.huggingface.co/)
  用于模型、数据、微调和开源工具实践；结论仍需实验验证。

## Gaps

- 用户的 pytest、NumPy、概率和矩阵起点尚未由陌生任务验证。
- 每周实际投入时间、API 预算和 GPU 条件尚未确定。
- API、模型名称、价格、上下文限制和托管评估接口会变化；进入相应单元时必须核验官方当前文档。
- 两份 D 盘教学指南是导航材料，可能落后于源码；每次进入具体节点前需对照当前仓库。
