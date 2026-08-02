(() => {
  const main = document.querySelector("main");
  if (!main || document.querySelector(".course-context-bar")) return;
  const filename = location.pathname.split("/").pop() || "index.html";
  const positions = {
    "index.html": "唯一课程入口",
    "0001-deterministic-gate.html": "阶段 A · 环 0 · 已验证能力 LR 0001 细节",
    "0002-single-row-vs-batch.html": "阶段 A · 环 0 · 已验证能力 LR 0002 细节",
    "0003-status-controls-next-action.html": "阶段 A · 环 0 · 已验证能力 LR 0003 细节",
    "0004-two-workers-one-task.html": "阶段 A · 环 0 · 已验证能力 LR 0004 细节",
    "0005-save-claim-before-external-call.html": "阶段 A · 环 0 · 已验证能力 LR 0005 细节",
    "0006-bounded-retry.html": "阶段 A · 环 0 · 已验证能力 LR 0006 细节",
    "0007-idempotent-import.html": "阶段 A · 环 0 · 已验证能力 LR 0007 细节",
    "0008-find-the-owning-module.html": "阶段 A · 环 0 · 已验证能力 LR 0008 细节",
    "0009-output-is-not-action.html": "阶段 A · 环 1 · 正式会话 3 · 问题三候选材料",
    "0010-state-and-permitted-actions.html": "阶段 A · 环 1 · 正式会话 1（已完成）",
    "0011-integrated-review-established-capabilities.html": "阶段 A · 环 0 · 综合复习 R1",
    "0012-failure-retry-stop.html": "阶段 A · 环 1 · 正式会话 2（当前）",
    "0001-python-basics-playground.html": "阶段 A · 环 1 · Python 补充练习",
    "prototype-guided-session.html": "教学设计归档 · 不承担课程进度",
    "0001-first-terms.html": "全课程 · 跨会话术语参考",
    "0002-course-progress.html": "全课程 · 四阶段十七环完整路线",
    "0003-model-system-action-card.html": "阶段 A · 环 1 · 正式会话 3 · 问题三参考卡",
    "0004-session-page-contract.html": "全课程 · 学习会话页面规范",
    "0005-final-capabilities.html": "全课程 · 最终能力契约",
  };
  const inSubdirectory = /\/(lessons|practice|reference)\//.test(location.pathname);
  const prefix = inSubdirectory ? "../" : "";
  const position = document.body.dataset.routePosition || positions[filename] || "课程支持页面";
  const bar = document.createElement("aside");
  bar.className = "course-context-bar";
  bar.setAttribute("aria-label", "全课程统一目标与当前位置");
  bar.innerHTML = `<div><strong>最终目标</strong><span>独立设计、实现、评估和维护可靠、受控、可恢复的 LLM 工作流或 RAG Agent，并理解关键数学、张量、模型与系统机制。</span></div><div><strong>当前位置</strong><span>${position}</span></div><nav aria-label="全课程入口"><a href="${prefix}reference/0002-course-progress.html">完整路线</a><a href="${prefix}reference/0005-final-capabilities.html">最终能力契约</a></nav>`;
  main.prepend(bar);
})();
