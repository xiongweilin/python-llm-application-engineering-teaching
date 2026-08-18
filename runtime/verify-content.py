"""Verify the structure and local links of the course artifact."""

from __future__ import annotations

import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
BANNED_TEXT = (
    "旧课程",
    "outputs\\python-teaching",
    "outputs/python-teaching",
    "outputs\\llm-application-engineering-teaching",
    "outputs/llm-application-engineering-teaching",
    "2026-07-18\\60-90-5-6-text-12",
)
STALE_ACTIVE_ROUTE_TEXT = (
    "当前六个正式会话",
    "当前六个会话",
    "会话 1–6",
    "会话 3–6",
    "未来正式会话 5",
    "未来正式会话 6",
    "正式会话 6“模型候选与已授权行动”",
    "六会话是首段",
    "状态与 Python 控制",
)
RETIRED_CONTENT_FILES = (
    "MISSION.md",
    "TEACHING-OVERVIEW.md",
    "SESSION-DESIGN-PROPOSAL.md",
    "reference/0004-session-page-contract.html",
    "reference/0005-final-capabilities.html",
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()
        self.scripts: list[str] = []
        self._script_parts: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"] or "")
        if tag in {"a", "link"} and attributes.get("href"):
            self.links.append(attributes["href"] or "")
        if tag == "script" and not attributes.get("src"):
            self._script_parts = []

    def handle_data(self, data: str) -> None:
        if self._script_parts is not None:
            self._script_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._script_parts is not None:
            self.scripts.append("".join(self._script_parts))
            self._script_parts = None


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def check_node_syntax(script: str, page: Path, number: int, failures: list[str]) -> None:
    result = subprocess.run(
        ["node", "--check", "-"],
        input=script,
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=False,
    )
    if result.returncode:
        details = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else "unknown error"
        failures.append(f"JavaScript syntax: {page.relative_to(ROOT)} script {number}: {details}")


def main() -> int:
    failures: list[str] = []
    lessons = sorted((ROOT / "lessons").glob("*.html"))
    records = sorted((ROOT / "learning-records").glob("*.md"))
    if len(lessons) != 12:
        failures.append(f"expected 12 lessons, found {len(lessons)}")
    if len(records) != 11:
        failures.append(f"expected 11 learning records, found {len(records)}")

    required = (
        ROOT / "index.html",
        ROOT / "assets" / "course.css",
        ROOT / "assets" / "course-context.js",
        ROOT / "assets" / "wallhaven-6ld8xl.jpg",
        ROOT / "practice" / "0001-python-basics-playground.html",
        ROOT / "reference" / "0001-first-terms.html",
        ROOT / "reference" / "0002-course-progress.html",
        ROOT / "reference" / "0003-model-system-action-card.html",
        ROOT / "lessons" / "0010-state-and-permitted-actions.html",
        ROOT / "lessons" / "0011-integrated-review-established-capabilities.html",
        ROOT / "lessons" / "0012-failure-retry-stop.html",
        ROOT / "learning-records" / "0011-implement-and-transfer-state-transitions.md",
        ROOT / "SESSION-PAGE-CONTRACT.md",
        ROOT / "FINAL-CAPABILITY-CONTRACT.md",
        ROOT / "docs" / "decisions" / "0001-finite-computable-curriculum-core.md",
        ROOT / "docs" / "decisions" / "0003-reactivation-learner-and-fading-support.md",
        ROOT / "docs" / "decisions" / "0004-map-before-expression-edit.md",
        ROOT / "docs" / "decisions" / "0005-phase-a-translation-layer-and-diagnostic-help.md",
        ROOT / "docs" / "decisions" / "0006-phase-a-semantic-types-and-non-echo-evidence.md",
        ROOT / "docs" / "decisions" / "0007-phase-a-whole-work-unit-cycle.md",
        ROOT / "docs" / "decisions" / "0008-open-judgment-and-threshold-switch.md",
        ROOT / "docs" / "decisions" / "0009-domain-thresholds-judgment-history-and-ai-intervention.md",
    )
    for path in required:
        if not path.is_file():
            failures.append(f"missing required file: {path.relative_to(ROOT)}")
    for relative in RETIRED_CONTENT_FILES:
        if (ROOT / relative).exists():
            failures.append(f"retired duplicate content file still exists: {relative}")

    shared_css_path = ROOT / "assets" / "course.css"
    if shared_css_path.is_file():
        shared_css = shared_css_path.read_text(encoding="utf-8")
        for marker in ("--course-accent", "--course-card-alpha: 0", "--course-control-alpha: 0", "--course-border-alpha: 0", "--course-text-alpha: 1", "--course-image-brightness: 0.8", "--course-image-veil-alpha: 0.1", "--course-shadow: none", "rgb(255 253 248 / var(--course-card-alpha))", "rgb(24 36 52 / var(--course-card-alpha))", "rgb(25 37 54 / var(--course-text-alpha))", "rgb(255 255 255 / var(--course-control-alpha))", "rgb(24 36 52 / var(--course-image-veil-alpha))", "filter: brightness(var(--course-image-brightness))", "main *:not(#course-foreground-surface)::before", "background-color: transparent", "scrollbar-width: auto", "scrollbar-color: transparent transparent", "main *::-webkit-scrollbar", "main *::-webkit-scrollbar-thumb", "height: 12px", ".course-nav", ".course-context-bar", ".course-background-image", ".course-background-overlay", "opacity: 0.7", "prefers-reduced-motion: reduce", ".question-button", ".page-status", ".session-terms", ".term-grid", ".session-controls", ".prototype-switcher", ".completion", "textarea", "@media"):
            if marker not in shared_css:
                failures.append(f"missing shared CSS marker: {marker}")
        if "scrollbar-width: none" in shared_css:
            failures.append("shared CSS removes scrollbar interaction instead of only hiding its colors")
        without_comments = re.sub(r"/\*.*?\*/", "", shared_css, flags=re.DOTALL)
        if without_comments.count("{") != without_comments.count("}"):
            failures.append("unbalanced braces in assets/course.css")

    background_image_path = ROOT / "assets" / "wallhaven-6ld8xl.jpg"
    if background_image_path.is_file() and background_image_path.stat().st_size < 100_000:
        failures.append("shared course background image is unexpectedly small")

    required_text = {
        ROOT / "index.html": ("四个能力阶段", "阶段 A · 环 1", "正式会话 2", "受控重试：一个完整工作单元", "11 条", "17 环", "约 90–125", "最终能力契约", "数学、决策与多主体系统", "现实含义", "程序责任", "editable locus", "三个证据阶段", "课程如何切换学习方式", "开放问题窗口", "最低可判断能力", "127.0.0.1:8766"),
        ROOT / "README.md": ("Controlled retry: one complete work unit", "single complete retry work unit", "pattern acquisition", "controlled variation", "transfer/chunking", "worked trace", "editable loci", "R/T/P/M/D/X", "prediction-before-runtime", "line-by-line comments", "two coupled loops", "open-question window", "Minimum Viable Judgment", "minimum operational models", "J0", "J1", "applicability judgment", "AI intervention contract", "Modules, diagnostics, and authorization boundaries", "Active documents stay minimal but sufficient", "final-capability-to-gate coverage index"),
        ROOT / "FINAL-CAPABILITY-CONTRACT.md": ("## 主线建模原则", "minimum operational models", "MVJ_Python", "MVJ_Probability", "## 1. 数学语言、概率、统计与证据", "## 2. 线性代数与张量计算", "## 3. 微积分、决策与约束优化", "## 4. 状态演化、随机过程与序贯决策", "## 5. 语言模型核心计算", "## 6. Transformer 机制", "## 7. 嵌入、检索与 RAG", "## 8. 优化训练、数值精度与计算排错", "**主线核心：**", "**按需扩展：**", "不要求每位学习者实际开展系统性微调实验", "通信类", "平稳分布", "碰撞点（collider）", "d-分离（d-separation）", "离线有限模型、仿真或回放分析", "适用性判断", "邻近的真实子问题", "## 9. API、工作流、Agent 与人机合作", "## 10. 博弈、信息与有限机制分析", "## 11. 实验、因果评估与系统可靠性", "## 最终综合项目", "## 研究扩展范围"),
        ROOT / "reference" / "0002-course-progress.html": ("四个阶段", "十七个学习环", "约 90–125", "环 0", "环 16", "会话 2“受控重试：完整工作单元”", "完整范例与运行轨迹", "完整重建", "受控变化", "迁移与组块化", "候选值", "开放问题窗口", "最低可判断能力", "minimum operational models", "适用性判断", "邻近真实子问题", "当前阶段相称的条件变化", "会话 3“模块、诊断与授权边界”", "数学语言、概率、统计与证据", "线性代数与张量", "微积分、决策与约束优化", "状态演化、随机过程与序贯决策", "博弈、信息与有限机制分析", "语言模型核心计算", "Transformer 机制", "训练与数值核心", "按需扩展", "不要求实际完成系统微调", "嵌入、检索与 RAG", "Agent、运行决策与人机合作", "实验、因果评估与系统可靠性", "背门路径", "碰撞点（collider）", "最终能力契约", "离线有限模型、仿真或回放", "最终综合项目与论文阅读", "十一项最终能力如何落到路线", "最终能力—关口覆盖索引"),
        ROOT / "reference" / "0001-first-terms.html": ("跨会话中文术语总表", 'data-page-kind="reference"', 'data-route-position="跨会话中文术语总表"', "最终能力契约", "正式会话 1：状态与允许行动", "正式会话 2：受控重试", "完整重建", "指数退避"),
        ROOT / "NOTES.md": ("完整、可观察、可验证的工程工作单元", "模式获得", "受控变化", "迁移与组块化", "A1", "纵向切片", "会话 3“模块、诊断与授权边界”", "R/T/P/M/D/X", "两个循环", "开放问题窗口", "Minimum Viable Judgment", "Frame / Discriminate / Judge / Challenge / Revise", "逐行旁注", "再激活型学习者", "editable locus", "现实含义 → 程序责任 → 代码位置 → Python 写法 → 学生操作 → 运行验证", "pass", "阶段 A 出题审查", "候选值", "禁止答案回显题", "完整重建", "活动文档保持最小且充分"),
        ROOT / "RESOURCES.md": ("Commerce Orchestrator", "DeepSeek Harness", "教育领域模型", "统计决策", "凸优化与运筹", "Linear, MIP and CP-SAT Examples", "有限状态、序贯决策与在线学习", "实验设计与有限因果图", "Always Valid Inference", "DAGitty learning materials", "博弈与有限机制分析", "LoRA 的矩阵结构、rank 和参数量属于环 12 主线", "Research extensions"),
        ROOT / "SESSION-PAGE-CONTRACT.md": ("2026-08-18", "唯一最终能力事实源 → 阶段 → 学习环", "本会话中文术语", "完整、可观察、可验证的工程工作单元", "主要完整工作单元", "完整范例与运行轨迹", "完整模仿", "完整重建", "受控变化", "新情境迁移", "稳定骨架与可变参数", "两个循环", "开放问题窗口", "J0", "J1", "Minimum Viable Judgment", "MVJ_Python", "MVJ_Probability", "MVJ_Optimization", "MVJ_RAG", "行为契约 → 学习者先判断 → 实现或诊断", "AI intervention contract", "答案供给下降", "问题空间供给上升", "Frame", "Discriminate", "Judge", "Challenge", "Revise", "阶段 A 的证据坡度", "R = Recognize", "T = Trace", "P = Produce", "M = Modify", "D = Diagnose", "X = Transfer", "阶段 A 注意事项", "唯一未知量", "预测必须先于运行验证", "五类帮助", "scrollIntoView", "模块、诊断与授权边界", "四阶段、十七环"),
        ROOT / "docs" / "decisions" / "0001-finite-computable-curriculum-core.md": ("## 状态", "已接受", "有限表示、有限维、可计算优先", "主线知识", "完整证据清单", "## 未采用的方案", "## 后果"),
        ROOT / "docs" / "decisions" / "0002-guided-teaching-before-independent-transfer.md": ("## 状态", "示范优先、局部补全、有限迁移", "教师示范 → 共同追踪输入/输出 → 局部补全", "逐行旁注", "不能只给术语、规则和空白函数", "## 未采用的方案", "## 后果"),
        ROOT / "docs" / "decisions" / "0003-reactivation-learner-and-fading-support.md": ("## 状态", "再激活型学习者", "结构记忆仍在、符号检索失败", "帮助逐步淡出", "建议路径", "完整讲解", "## 未采用的方案", "## 后果"),
        ROOT / "docs" / "decisions" / "0004-map-before-expression-edit.md": ("## 状态", "attempt", "等待序列", "可观察对应关系/映射", "唯一可编辑位置", "## 未采用的方案", "## 后果"),
        ROOT / "docs" / "decisions" / "0005-phase-a-translation-layer-and-diagnostic-help.md": ("## 状态", "现实含义 → 程序责任 → 代码位置 → Python 写法 → 学生操作 → 运行验证", "术语来源", "三种难度", "五类帮助", "## 未采用的方案", "## 后果"),
        ROOT / "docs" / "decisions" / "0006-phase-a-semantic-types-and-non-echo-evidence.md": ("## 状态", "attempt", "delay", "是否等待", "候选值", "唯一未知量", "## 未采用的方案", "## 后果"),
        ROOT / "docs" / "decisions" / "0007-phase-a-whole-work-unit-cycle.md": ("## 状态", "完整、可观察、可验证的工程工作单元", "模式获得", "受控变化", "迁移与组块化", "完整重建", "R/T/P/M/D/X", "## 未采用的方案", "## 后果"),
        ROOT / "docs" / "decisions" / "0008-open-judgment-and-threshold-switch.md": ("## 状态", "开放问题窗口", "Minimum Viable Judgment", "两个循环", "行为契约 → 学习者先判断 → 实现或诊断", "Frame", "Discriminate", "Judge", "Challenge", "Revise", "## 未采用的方案", "## 后果"),
        ROOT / "docs" / "decisions" / "0009-domain-thresholds-judgment-history-and-ai-intervention.md": ("## 状态", "分领域阈值", "J0", "J1", "AI intervention contract", "答案供给下降", "问题空间供给上升", "适用性判断", "邻近真实子问题", "## 未采用的方案", "## 后果"),
    }
    for path, markers in required_text.items():
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                failures.append(f"missing course-map marker in {path.relative_to(ROOT)}: {marker}")

    route = (ROOT / "reference" / "0002-course-progress.html").read_text(encoding="utf-8")
    for marker in ("中心问题：", "前置能力：", "主线知识：", "明确不包含：", "编程或计算落点：", "跨项目迁移：", "与下一环接口："):
        if route.count(marker) != 6:
            failures.append(f"modified ring responsibility field must appear exactly six times: {marker} ({route.count(marker)})")
    if route.count("通过关口") < 6:
        failures.append("modified rings must retain six explicit passing gates")

    coverage_rows = {
        capability: body
        for capability, body in re.findall(
            r'<tr data-capability="([A-Z]+-?[0-9]*)">(.*?)</tr>', route, flags=re.DOTALL
        )
    }
    expected_coverage = {
        "FC-01": ("LLN/CLT", "第一类/第二类错误", "校准", "Hoeffding bound"),
        "FC-02": ("投影", "特征值/特征向量", "SVD", "广播"),
        "FC-03": ("Jacobian", "Hessian", "LP/MIP", "Lagrange/KKT", "信息价值"),
        "FC-04": ("Markov", "MDP", "POMDP", "UCB/Thompson", "简单排队"),
        "FC-05": ("top-k/top-p", "交叉熵", "KL", "困惑度"),
        "FC-06": ("Q/K/V", "√dₖ", "KV cache", "shape/mask"),
        "FC-07": ("精确/近似最近邻", "切分", "索引版本", "Recall@k/MRR/nDCG"),
        "FC-08": ("反向传播", "SGD/动量/Adam", "LoRA", "log-sum-exp", "粗粒度资源估算"),
        "FC-09": ("JSON Schema", "重试/幂等/补偿", "人工容量", "安全降级"),
        "FC-10": ("纯/混合纳什均衡", "贝叶斯—纳什均衡", "DSIC/BIC", "IR", "稳定匹配"),
        "FC-11": ("estimand/ATE", "统计功效", "背门路径", "碰撞点", "SLO/上线门槛/停止/回滚"),
        "CAPSTONE": ("决策、策略、序贯、机制、因果、工程六组证据", "持久状态", "故障注入"),
    }
    if set(coverage_rows) != set(expected_coverage):
        failures.append(
            f"capability-gate coverage rows mismatch: expected {sorted(expected_coverage)}, got {sorted(coverage_rows)}"
        )
    for capability, markers in expected_coverage.items():
        row = coverage_rows.get(capability, "")
        for marker in markers:
            if marker not in row:
                failures.append(f"capability-gate coverage missing {capability}: {marker}")

    active_scope_files = (
        ROOT / "index.html",
        ROOT / "README.md",
        ROOT / "NOTES.md",
        ROOT / "reference" / "0002-course-progress.html",
    )
    for path in active_scope_files:
        text = path.read_text(encoding="utf-8")
        if "90–120" in text:
            failures.append(f"stale total session range in {path.relative_to(ROOT)}: 90–120")

    terms_page = (ROOT / "reference" / "0001-first-terms.html").read_text(encoding="utf-8")
    if '<body data-page-kind="reference" data-route-position="跨会话中文术语总表">' not in terms_page:
        failures.append("terms page must declare page kind and route position")

    boundary_card = (ROOT / "reference" / "0003-model-system-action-card.html").read_text(encoding="utf-8")
    for marker in ('data-route-position="阶段 A · 环 1 · 正式会话 3 · 问题三参考卡"', "最终能力契约"):
        if marker not in boundary_card:
            failures.append(f"boundary card missing page identity or capability entry: {marker}")

    homepage = (ROOT / "index.html").read_text(encoding="utf-8")
    for marker in ("sessionStorage.setItem(tokenStorageKey", "sessionStorage.getItem(tokenStorageKey", "history.replaceState", "sessionStorage.removeItem(tokenStorageKey"):
        if marker not in homepage:
            failures.append(f"missing persistent shutdown-token behavior: {marker}")

    context_script_path = ROOT / "assets" / "course-context.js"
    if context_script_path.is_file():
        context_script = context_script_path.read_text(encoding="utf-8")
        for marker in ("最终目标", "当前位置", "完整路线", "最终能力契约", "阶段 A · 环 1", "正式会话 3 · 问题三", "四阶段十七环完整路线", "course-background-image", "assets/wallhaven-6ld8xl.jpg", "prefers-reduced-motion: reduce", "image.decoding", "document.body.prepend(image)", ".step-strip, .chain, .logic-path", "maxScrollLeft", "event.preventDefault()", "passive: false"):
            if marker not in context_script:
                failures.append(f"missing shared course-context marker: {marker}")
        check_node_syntax(context_script, context_script_path, 1, failures)

    interactive_contracts = {
        ROOT / "practice" / "0001-python-basics-playground.html": (
            'id="transfer-answer"',
            'reflectionKey("transfer"',
            'reflectionFor("transfer"',
            'RECOMMENDED_TASK_INDEX = 1',
            '阶段 A 的翻译顺序',
            '现实含义 → 程序责任 → 代码位置 → Python 写法 → 学生操作 → 运行验证',
        ),
        ROOT / "lessons" / "0008-find-the-owning-module.html": (
            'id="recall-answer"',
            'id="module-answer"',
            'id="copy-lesson"',
            'localStorage.setItem(storageKey',
        ),
        ROOT / "lessons" / "0009-output-is-not-action.html": (
            'data-answer',
            'id="copy-answers"',
            'localStorage.setItem(storageKey',
        ),
        ROOT / "practice" / "prototype-guided-session.html": (
            'data-variant="A"',
            'data-variant="B"',
            'data-variant="C"',
            'class="prototype-switcher"',
            'params.set("variant"',
        ),
        ROOT / "lessons" / "0010-state-and-permitted-actions.html": (
            'data-page-kind="completed-session"',
            '正式会话 1 已完成',
            'data-step="0"',
            'data-task="1"',
            'data-task="2"',
            'data-task="3"',
            'id="core-code"',
            'id="transfer-code"',
            'id="copy-submission"',
            '本会话中文术语',
            '跨会话总术语表',
            'localStorage.setItem(STORAGE_PREFIX',
            'function buildWorkerSource()',
            'CHECK_MODE',
            '阶段 A 翻译地图',
            '复习帮助（五类分开）',
            'data-help-kind="task"',
            'data-help-kind="locus"',
            'data-help-kind="syntax"',
            'data-help-kind="reasoning"',
            'data-help-kind="answer"',
            'activeStep.getBoundingClientRect',
            'id="core-key"',
            'id="core-guard"',
            'id="core-raise"',
            'id="core-return"',
            'id="transfer-cancel-line"',
            'syncCoreSource',
            'syncTransferSource',
            'syntax-visible',
        ),
        ROOT / "lessons" / "0011-integrated-review-established-capabilities.html": (
            'data-page-kind="review-session"',
            'data-step="0"',
            'data-task="1"',
            'data-task="2"',
            'data-task="3"',
            'id="check-recall"',
            'id="check-incident"',
            'id="check-transfer"',
            'id="copy-review"',
            '本会话中文术语',
            '不改变正式会话进度',
            '不会重复创建记录',
            'localStorage.setItem(STORAGE_PREFIX',
            '阶段 A 翻译地图',
            '当前复习帮助（五类分开）',
            'data-help-kind="task"',
            'data-help-kind="locus"',
            'data-help-kind="syntax"',
            'data-help-kind="reasoning"',
            'data-help-kind="answer"',
            'activeStep.getBoundingClientRect',
        ),
        ROOT / "lessons" / "0012-failure-retry-stop.html": (
            'data-page-kind="formal-session"',
            'data-session-id="S02"',
            'data-step="0"',
            'data-step="4"',
            'data-step-target="0"',
            'data-step-target="4"',
            'data-task="1"',
            'data-task="3"',
            'id="retry-rebuild-code"',
            'id="retry-transfer-code"',
            'id="actual-minutes"',
            'id="copy-submission"',
            'TemporaryError',
            'PermanentError',
            'sleep_fn',
            '指数退避',
            '1 个主要工作单元',
            '3 类能力证据',
            '完整理解与重建',
            '受控修改',
            '新情境迁移',
            '现实含义 → 程序责任 → 代码位置 → Python 写法 → 学生操作 → 运行验证',
            'course-session-0012-v8-whole-work-unit-',
            'retry-imitation-code',
            'imitation-notes',
            '输入时就近提醒',
            '忘记某一行时，直接看上面的教师范例',
            'retry-rebuild-code',
            'retry-variation-code',
            'teacher-example',
            'start-rebuild',
            'reopen-example',
            'def f(...):',
            '案例 A：第一次暂时失败，第二次成功',
            '案例 B：第一次就是永久失败',
            '案例 C：一直暂时失败，max_attempts=3',
            '把我的完整重建带入这里',
            'policy-next-delay',
            'policy-last-wait',
            'check-policy',
            'scrollIntoView({behavior: "smooth", block: "start"})',
            'data-hint-level="syntax"',
            'data-hint-level="reasoning"',
            'data-hint-level="answer"',
            '当前任务帮助（五类分开）',
            'data-help-kind="task"',
            'data-help-kind="locus"',
            'data-help-kind="syntax"',
            'data-help-kind="reasoning"',
            'data-help-kind="answer"',
            '现实含义 → 程序责任 → 代码位置 → Python 写法 → 学生操作 → 运行验证',
            '阶段 A 注意事项',
            '候选时长不等于一定发生的等待',
            '本会话中文术语',
            'localStorage.setItem(STORAGE_PREFIX',
            'aria-current", "step"',
            'chips.forEach((chip, index) => chip.addEventListener("click"',
            'function buildWorkerSource()',
            'CHECK_MODE',
            '达到标准后老师直接给出下一会话',
        ),
    }
    for path, markers in interactive_contracts.items():
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                failures.append(f"missing interaction marker in {path.relative_to(ROOT)}: {marker}")

    session_two = (ROOT / "lessons" / "0012-failure-retry-stop.html").read_text(encoding="utf-8")
    if 'window.scrollTo({top:0,behavior:"smooth"});}' in session_two:
        failures.append("session 2 must scroll to the active step instead of always returning to the page top")
    step_targets = [int(value) for value in re.findall(r'data-step-target="(\d+)"', session_two)]
    if step_targets != list(range(5)):
        failures.append(f"session 2 clickable stage targets must be exactly 0..4, got {step_targets}")

    prototype = (ROOT / "practice" / "prototype-guided-session.html").read_text(encoding="utf-8")
    if "localStorage" in prototype or "sessionStorage" in prototype:
        failures.append("prototype must not persist answers or progress")

    lesson_roles = {
        **{lesson_number: "completed-review" for lesson_number in range(1, 9)},
        9: "candidate-reference",
        10: "completed-session",
        11: "review-session",
        12: "formal-session",
    }
    for lesson_number, expected_role in lesson_roles.items():
        lesson = next((ROOT / "lessons").glob(f"{lesson_number:04d}-*.html"))
        text = lesson.read_text(encoding="utf-8")
        marker = f'data-page-kind="{expected_role}"'
        if marker not in text:
            failures.append(f"wrong or missing page role in {lesson.relative_to(ROOT)}: expected {expected_role}")

    for lesson_number in range(1, 9):
        lesson = next((ROOT / "lessons").glob(f"{lesson_number:04d}-*.html"))
        text = lesson.read_text(encoding="utf-8")
        for forbidden in ('href="../practice/0001-python-basics-playground.html">当前练习', "用自己的话告诉老师"):
            if forbidden in text:
                failures.append(f"completed review still presents active-course wording in {lesson.relative_to(ROOT)}: {forbidden}")
        if re.search(r"第[一二三四五六七八九十0-9]+课|前[一二三四五六七八九十]+课", text):
            failures.append(f"completed review still uses old lesson numbering as route wording: {lesson.relative_to(ROOT)}")

    candidate = (ROOT / "lessons" / "0009-output-is-not-action.html").read_text(encoding="utf-8")
    for marker in ("正式会话 3", "模块、诊断与授权边界", "问题三", "模型候选与已授权行动", "当前未开始", "不承担当前进度"):
        if marker not in candidate:
            failures.append(f"missing candidate-session position in lessons/0009-output-is-not-action.html: {marker}")

    boundary_card = (ROOT / "reference" / "0003-model-system-action-card.html").read_text(encoding="utf-8")
    for marker in ('data-page-kind="candidate-reference"', "正式会话 3", "问题三", "模型候选与已授权行动", "当前未开始", "返回当前正式会话"):
        if marker not in boundary_card:
            failures.append(f"missing reference-card session position: {marker}")

    session_three_sources = (
        ROOT / "SESSION-PAGE-CONTRACT.md",
        ROOT / "NOTES.md",
        ROOT / "reference" / "0002-course-progress.html",
    )
    for path in session_three_sources:
        text = path.read_text(encoding="utf-8")
        for marker in ("模块、诊断与授权边界", "模块责任与调用链", "traceback 与测试诊断", "模型候选与已授权行动"):
            if marker not in text:
                failures.append(f"session 3 route mismatch in {path.relative_to(ROOT)}: missing {marker}")

    active_route_files = (
        ROOT / "README.md",
        ROOT / "NOTES.md",
        ROOT / "index.html",
        ROOT / "assets" / "course-context.js",
        ROOT / "SESSION-PAGE-CONTRACT.md",
        *sorted((ROOT / "lessons").glob("*.html")),
        *sorted((ROOT / "practice").glob("*.html")),
        *sorted((ROOT / "reference").glob("*.html")),
    )
    for path in active_route_files:
        text = path.read_text(encoding="utf-8")
        for stale in STALE_ACTIVE_ROUTE_TEXT:
            if stale in text:
                failures.append(f"stale active route wording in {path.relative_to(ROOT)}: {stale}")

    completed_session = (ROOT / "lessons" / "0010-state-and-permitted-actions.html").read_text(encoding="utf-8")
    if completed_session.count('data-task="') != 3:
        failures.append("completed formal session must retain exactly three related tasks")

    formal_session = (ROOT / "lessons" / "0012-failure-retry-stop.html").read_text(encoding="utf-8")
    if formal_session.count("任务 1 ·") != 1 or formal_session.count("任务 2 ·") != 1 or formal_session.count("任务 3 ·") != 1:
        failures.append("formal session 2 must contain the three complete-work-unit evidence stages")
    if formal_session.count('class="session-step') != 5:
        failures.append("formal session 2 must contain five focus stages including map and submission")
    if formal_session.count('class="stage-chip') != 5:
        failures.append("formal session 2 stage strip must contain five chips")
    if not re.search(r'<textarea id="retry-imitation-code"[^>]*></textarea>', formal_session):
        failures.append("complete imitation editor must be genuinely blank until the learner types")
    if 'id="policy-expression"' in formal_session:
        failures.append("controlled variation must not expose a second standalone expression input")
    for marker in ('id="teacher-example"', 'id="start-rebuild"', 'id="reopen-example"', '案例 A：第一次暂时失败，第二次成功', '案例 B：第一次就是永久失败', '案例 C：一直暂时失败，max_attempts=3'):
        if marker not in formal_session:
            failures.append(f"formal session 2 missing whole-unit interaction marker: {marker}")

    review_session = (ROOT / "lessons" / "0011-integrated-review-established-capabilities.html").read_text(encoding="utf-8")
    if review_session.count('data-task="') != 3:
        failures.append("review session must contain exactly three integrated tasks")

    for lesson_number in range(1, 8):
        lesson = next((ROOT / "lessons").glob(f"{lesson_number:04d}-*.html"))
        text = lesson.read_text(encoding="utf-8")
        if '<input type="radio"' not in text or "检查答案" not in text:
            failures.append(f"missing immediate quiz feedback in {lesson.relative_to(ROOT)}")

    local_sources = (
        Path(r"D:\agent\ratio\电商工作流项目\README.md"),
        Path(r"D:\agent\deepseek-harness\README.md"),
        Path(r"D:\agent\ratio\领域模型\计算机领域模型.md"),
        Path(r"D:\agent\ratio\领域模型\教育领域模型.md"),
        Path(r"D:\agent\ratio\有限宇宙\有限变化实践.md"),
    )
    for path in local_sources:
        if not path.is_file():
            failures.append(f"missing local teaching source: {path}")

    text_files = [*ROOT.rglob("*.md"), *ROOT.rglob("*.html")]
    for path in text_files:
        text = path.read_text(encoding="utf-8")
        for banned in BANNED_TEXT:
            if banned.casefold() in text.casefold():
                failures.append(f"banned source/migration wording in {path.relative_to(ROOT)}: {banned}")

    pages: dict[Path, PageParser] = {}
    for page in ROOT.rglob("*.html"):
        page_text = page.read_text(encoding="utf-8")
        if not re.search(r'<link\s+[^>]*rel=["\']icon["\']', page_text, flags=re.IGNORECASE):
            failures.append(f"missing favicon declaration: {page.relative_to(ROOT)}")
        theme_links = re.findall(r'<link\s+[^>]*href=["\']([^"\']*assets/course\.css)["\']', page_text, flags=re.IGNORECASE)
        if len(theme_links) != 1:
            failures.append(f"expected one shared theme link in {page.relative_to(ROOT)}, found {len(theme_links)}")
        elif page_text.find(theme_links[0]) < page_text.rfind("</style>"):
            failures.append(f"shared theme must load after inline styles: {page.relative_to(ROOT)}")
        context_links = re.findall(r'<script\s+[^>]*src=["\']([^"\']*assets/course-context\.js)["\']', page_text, flags=re.IGNORECASE)
        if len(context_links) != 1:
            failures.append(f"expected one shared course-context script in {page.relative_to(ROOT)}, found {len(context_links)}")
        if page != ROOT / "index.html" and not re.search(r"<nav\b", page_text, flags=re.IGNORECASE):
            failures.append(f"missing course navigation: {page.relative_to(ROOT)}")
        parser = parse_page(page)
        pages[page.resolve()] = parser
        for number, script in enumerate(parser.scripts, start=1):
            if script.strip():
                check_node_syntax(script, page, number, failures)

    if len(pages) != 18:
        failures.append(f"expected 18 HTML pages, found {len(pages)}")

    for page, parser in pages.items():
        for href in parser.links:
            parts = urlsplit(href)
            if parts.scheme or parts.netloc or href.startswith(("mailto:", "javascript:")):
                continue
            target = page if not parts.path else (page.parent / unquote(parts.path)).resolve()
            if not target.exists():
                failures.append(f"broken local link: {page.relative_to(ROOT)} -> {href}")
                continue
            if parts.fragment and target.suffix.lower() == ".html":
                target_parser = pages.get(target.resolve()) or parse_page(target)
                if parts.fragment not in target_parser.ids:
                    failures.append(f"missing fragment: {page.relative_to(ROOT)} -> {href}")

    output = {
        "passed": not failures,
        "lessons": len(lessons),
        "learning_records": len(records),
        "html_pages": len(pages),
        "themed_pages": sum(1 for page in pages if "assets/course.css" in page.read_text(encoding="utf-8")),
        "failures": failures,
    }
    import json

    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
