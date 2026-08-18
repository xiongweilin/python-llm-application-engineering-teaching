(() => {
  const main = document.querySelector("main");
  if (!main) return;
  const filename = location.pathname.split("/").pop() || "index.html";
  const inSubdirectory = /\/(lessons|practice|reference)\//.test(location.pathname);
  const prefix = inSubdirectory ? "../" : "";
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!reducedMotion && !document.querySelector(".course-background-image")) {
    const image = document.createElement("img");
    image.className = "course-background-image";
    image.src = `${prefix}assets/wallhaven-6ld8xl.jpg`;
    image.alt = "";
    image.decoding = "async";
    image.setAttribute("aria-hidden", "true");
    image.tabIndex = -1;

    const overlay = document.createElement("div");
    overlay.className = "course-background-overlay";
    overlay.setAttribute("aria-hidden", "true");

    document.body.prepend(overlay);
    document.body.prepend(image);
  }

  const horizontalScrollers = main.querySelectorAll(".step-strip, .chain, .logic-path");
  for (const scroller of horizontalScrollers) {
    if (!scroller.hasAttribute("tabindex")) scroller.tabIndex = 0;
    scroller.addEventListener("wheel", (event) => {
      if (event.ctrlKey || event.shiftKey || Math.abs(event.deltaX) >= Math.abs(event.deltaY)) return;
      const maxScrollLeft = scroller.scrollWidth - scroller.clientWidth;
      if (maxScrollLeft <= 0) return;
      const delta = event.deltaY;
      const atStart = scroller.scrollLeft <= 0;
      const atEnd = scroller.scrollLeft >= maxScrollLeft - 1;
      if ((delta < 0 && atStart) || (delta > 0 && atEnd)) return;
      scroller.scrollLeft = Math.max(0, Math.min(maxScrollLeft, scroller.scrollLeft + delta));
      event.preventDefault();
    }, { passive: false });
  }

  if (document.querySelector(".course-context-bar")) return;
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
    "0012-failure-retry-stop.html": "阶段 A · 环 1 · 正式会话 2 · 受控重试工作单元（当前）",
    "0001-python-basics-playground.html": "阶段 A · 环 1 · Python 补充练习",
    "prototype-guided-session.html": "教学设计归档 · 不承担课程进度",
    "0001-first-terms.html": "全课程 · 跨会话术语参考",
    "0002-course-progress.html": "全课程 · 四阶段十七环完整路线",
    "0003-model-system-action-card.html": "阶段 A · 环 1 · 正式会话 3 · 问题三参考卡",
  };
  const position = document.body.dataset.routePosition || positions[filename] || "课程支持页面";
  const bar = document.createElement("aside");
  bar.className = "course-context-bar";
  bar.setAttribute("aria-label", "全课程统一目标与当前位置");
  bar.innerHTML = `<div><strong>最终目标</strong><span>独立交付可靠、受控、可恢复的 LLM 工作流或 RAG Agent，并在可计算模型中验证决策、序贯策略、人机分工与有限机制。</span></div><div><strong>当前位置</strong><span>${position}</span></div><nav aria-label="全课程入口"><a href="${prefix}reference/0002-course-progress.html">完整路线</a><a href="${prefix}FINAL-CAPABILITY-CONTRACT.md">最终能力契约</a></nav>`;
  main.prepend(bar);
})();
