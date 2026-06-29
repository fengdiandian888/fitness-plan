/* ============================================================
   减脂教练 App · 共享 JS v4.0
   用途：Tab 栏注入、B站视频懒加载、通用工具函数、用户画像管理
   使用：页面 <head> 中 <link rel="stylesheet" href="shared.css">
         body 末尾 <script src="shared.js"></script>
   ============================================================ */
(function (global) {
  'use strict';

  // =========== 检查用户画像引导页 ===========
  function checkOnboarding() {
    var currentPage = window.location.pathname.split('/').pop();
    if (currentPage === 'onboarding.html') return;
    var done = localStorage.getItem('fit_onboarding_done');
    if (!done && currentPage !== 'onboarding.html') {
      window.location.href = 'onboarding.html';
      return false;
    }
    return true;
  }
  
  if (!checkOnboarding()) return;

  // =========== 页面元数据（告诉 shared.js 当前页是哪一个）===========
  // 页面自己在 <script> 中设置 window.PAGE_META = { key:'today', dark:false }
  const PAGE = Object.assign(
    {
      key: 'today',          // home | today | follow
      dark: false,           // 是否启用深色主题
      showBottomNav: true,   // 是否显示底部导航（默认显示）
      title: '减脂计划'
    },
    global.PAGE_META || {}
  );

  // =========== 应用主题（深色 body 添加 class）===========
  if (PAGE.dark) {
    document.body.classList.add('dark');
  }

  // =========== 导航栏配置（精简为3个导航项）===========
  const NAV_ITEMS = [
    { key: 'home',   label: '🏠 首页',         href: 'index.html' },
    { key: 'today',  label: '📋 今日计划',     href: '今日计划.html' },
    { key: 'follow', label: '💪 训练跟练',     href: '减脂训练日跟练_三分化.html' }
  ];

  // =========== 注入底部导航栏（所有页面都显示）===========
  function renderBottomNav() {
    if (document.querySelector('nav.bottom-nav')) return;

    const nav = document.createElement('nav');
    nav.className = 'tab-bar bottom-nav';
    nav.style.cssText = 'position:fixed;bottom:0;left:0;right:0;background:rgba(255,255,255,0.92);backdrop-filter:blur(14px);border-top:1px solid var(--border);border-bottom:none;z-index:100;';
    NAV_ITEMS.forEach(function (item) {
      const a = document.createElement('a');
      a.href = item.href;
      a.textContent = item.label;
      if (item.key === PAGE.key) a.classList.add('active');
      nav.appendChild(a);
    });
    document.body.appendChild(nav);
    document.body.style.paddingBottom = '68px';
  }

  // =========== B 站视频懒加载 ===========
  function setupBiliVideos() {
    document.querySelectorAll('[data-bvid]').forEach(function (el) {
      if (el.classList.contains('bili-rendered')) return;
      el.classList.add('bili-rendered');
      const bvid = el.getAttribute('data-bvid');
      const title = el.getAttribute('data-title') || '';
      renderBiliCard(el, bvid, title);
    });
  }

  function renderBiliCard(container, bvid, title) {
    if (!bvid) return;
    const card = document.createElement('div');
    card.className = 'vid-card';
    card.innerHTML =
      '<div class="vid-meta">' +
        '<span class="vid-icon">▶</span>' +
        '<span>' + (title || 'B 站跟练视频 · ' + bvid) + '</span>' +
      '</div>' +
      '<div class="vid-lazy" data-src="' + bvid + '"></div>';
    container.appendChild(card);
    const lazy = card.querySelector('.vid-lazy');
    lazy.addEventListener('click', function () {
      const iframe = document.createElement('iframe');
      iframe.src =
        'https://player.bilibili.com/player.html?bvid=' + bvid +
        '&page=1&high_quality=1&autoplay=1';
      iframe.setAttribute('allow', 'fullscreen');
      iframe.setAttribute('scrolling', 'no');
      iframe.setAttribute('frameborder', '0');
      lazy.parentNode.replaceChild(iframe, lazy);
    });
  }

  // =========== 通用：渲染动作清单（基于 FIT.moves 的统一格式）===========
  function renderMoves(containerId, moves) {
    const el = document.getElementById(containerId);
    if (!el || !Array.isArray(moves)) return;
    const list = document.createElement('div');
    list.className = 'move-list';
    moves.forEach(function (m, i) {
      if (!m || !m.name) return;
      const row = document.createElement('div');
      row.className = 'move-row';
      row.innerHTML =
        '<span class="mv-idx">' + (i + 1) + '</span>' +
        '<span class="mv-name">' + m.name + '</span>' +
        '<span class="mv-sets">' + (m.sets || '') + '</span>' +
        '<span class="mv-rest">' + (m.rest || '') + '</span>';
      list.appendChild(row);
    });
    el.appendChild(list);
  }

  // =========== Toast 提示（保存成功等）===========
  let toastTimer = null;
  function toast(msg) {
    let el = document.getElementById('app-toast');
    if (!el) {
      el = document.createElement('div');
      el.id = 'app-toast';
      el.className = 'save-flash';
      document.body.appendChild(el);
    }
    el.textContent = msg;
    el.classList.add('show');
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { el.classList.remove('show'); }, 1800);
  }

  // =========== 体重折线图（Canvas，替换原先手写版本）===========
  function renderWeightChart(canvasId, weightLog, startW, targetMin, targetMax) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const dpr = window.devicePixelRatio || 1;
    const width = canvas.clientWidth || 340;
    const height = 180;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    const ctx = canvas.getContext('2d');
    ctx.scale(dpr, dpr);

    const padding = { l: 36, r: 12, t: 14, b: 24 };
    const plotW = width - padding.l - padding.r;
    const plotH = height - padding.t - padding.b;

    // 数据范围
    const allVals = (weightLog || []).map(function (p) { return p.w; }).concat([startW, targetMin, targetMax]).filter(Number.isFinite);
    let yMin = Math.min.apply(null, allVals) - 0.5;
    let yMax = Math.max.apply(null, allVals) + 0.5;
    if (yMax - yMin < 2) { yMax = yMin + 2; }

    // 背景
    ctx.clearRect(0, 0, width, height);
    const grd = ctx.createLinearGradient(0, 0, 0, height);
    grd.addColorStop(0, 'rgba(249,115,22,0.08)');
    grd.addColorStop(1, 'rgba(249,115,22,0)');
    ctx.fillStyle = grd;
    ctx.fillRect(padding.l, padding.t, plotW, plotH);

    // 目标区间高亮
    const yTargetMin = padding.t + plotH - ((targetMin - yMin) / (yMax - yMin)) * plotH;
    const yTargetMax = padding.t + plotH - ((targetMax - yMin) / (yMax - yMin)) * plotH;
    ctx.fillStyle = 'rgba(96,165,250,0.12)';
    ctx.fillRect(padding.l, Math.min(yTargetMin, yTargetMax), plotW, Math.abs(yTargetMax - yTargetMin));

    // 水平网格线
    ctx.strokeStyle = 'rgba(0,0,0,0.05)';
    ctx.lineWidth = 1;
    ctx.font = '11px -apple-system, "PingFang SC", sans-serif';
    ctx.fillStyle = '#9ca3af';
    const steps = 4;
    for (let i = 0; i <= steps; i++) {
      const y = padding.t + (plotH * i) / steps;
      ctx.beginPath();
      ctx.moveTo(padding.l, y);
      ctx.lineTo(padding.l + plotW, y);
      ctx.stroke();
      const val = yMax - ((yMax - yMin) * i) / steps;
      ctx.fillText(val.toFixed(1), 4, y + 3);
    }

    if (!weightLog || weightLog.length === 0) return;

    // 数据线
    ctx.strokeStyle = '#f97316';
    ctx.lineWidth = 2.2;
    ctx.beginPath();
    weightLog.forEach(function (p, i) {
      const x = padding.l + (plotW * i) / Math.max(1, weightLog.length - 1);
      const y = padding.t + plotH - ((p.w - yMin) / (yMax - yMin)) * plotH;
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    ctx.stroke();

    // 数据点 + 填充
    ctx.fillStyle = 'rgba(249,115,22,0.18)';
    ctx.lineTo(padding.l + plotW, padding.t + plotH);
    ctx.lineTo(padding.l, padding.t + plotH);
    ctx.closePath();
    ctx.fill();

    ctx.fillStyle = '#fff';
    ctx.strokeStyle = '#f97316';
    ctx.lineWidth = 2;
    weightLog.forEach(function (p, i) {
      const x = padding.l + (plotW * i) / Math.max(1, weightLog.length - 1);
      const y = padding.t + plotH - ((p.w - yMin) / (yMax - yMin)) * plotH;
      ctx.beginPath();
      ctx.arc(x, y, 3.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
    });

    // 起始体重基准线（虚线）
    const yStart = padding.t + plotH - ((startW - yMin) / (yMax - yMin)) * plotH;
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = 'rgba(185,28,28,0.4)';
    ctx.lineWidth = 1.2;
    ctx.beginPath();
    ctx.moveTo(padding.l, yStart);
    ctx.lineTo(padding.l + plotW, yStart);
    ctx.stroke();
    ctx.setLineDash([]);
  }

  // =========== 体重进度条渲染 ===========
  function renderWeightProgress(containerId, startW, currentW, targetMin, targetMax) {
    const el = document.getElementById(containerId);
    if (!el) return;
    const total = Math.max(startW - targetMin, 1);
    const done = startW - currentW;
    let pct = Math.max(0, Math.min(100, (done / total) * 100));
    // 以 targetMin~targetMax 中点附近作为理想
    const targetMid = (targetMin + targetMax) / 2;
    const targetPct = ((startW - targetMid) / total) * 100;

    el.innerHTML =
      '<div class="progress-bar"><div class="progress-fill" style="width:' + pct.toFixed(1) + '%"></div></div>' +
      '<div class="progress-labels">' +
        '<span>起点 ' + startW.toFixed(1) + 'kg</span>' +
        '<span>目标 ' + targetMin.toFixed(1) + '–' + targetMax.toFixed(1) + 'kg</span>' +
      '</div>';
  }

  // =========== 通用：今日时间轴渲染（使用 plans 数据）===========
  function renderTimeline(trackId, plan, now) {
    const track = document.getElementById(trackId);
    if (!track || !plan || !plan.timeline) return;
    track.innerHTML = '';
    const nowMin = (now.getHours() * 60) + now.getMinutes();
    let bestIdx = -1;
    let bestDiff = Infinity;
    plan.timeline.forEach(function (item, i) {
      // item = { time:'07:00', type:'exercise', text:'' }
      const parts = (item.time || '00:00').split(':');
      const itemMin = parseInt(parts[0], 10) * 60 + parseInt(parts[1], 10);
      const diff = Math.abs(itemMin - nowMin);
      if (diff < bestDiff) { bestDiff = diff; bestIdx = i; }

      const el = document.createElement('div');
      el.className = 'tl-item';
      if (i === bestIdx) el.classList.add('now');
      el.innerHTML =
        '<div class="tl-time ' + (item.type || 'rest') + '">' + item.time + '</div>' +
        '<div class="tl-text">' + (item.text || '') + '</div>';
      track.appendChild(el);
    });

    // 滚动到当前
    setTimeout(function () {
      const parent = track.parentElement;
      const active = track.querySelector('.tl-item.now');
      if (active && parent) {
        parent.scrollLeft = active.offsetLeft - parent.clientWidth / 2 + active.clientWidth / 2;
      }
    }, 200);
  }

  // =========== 子 Tab（训练日 3× 分化等切换）===========
  function setupSubtabs(containerSelector) {
    document.querySelectorAll(containerSelector).forEach(function (root) {
      const btns = root.querySelectorAll('.subtab-btn');
      btns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          const target = btn.getAttribute('data-target');
          btns.forEach(function (b) { b.classList.remove('active'); });
          btn.classList.add('active');
          root.querySelectorAll('.tab-panel').forEach(function (p) { p.classList.remove('active'); });
          const panel = document.getElementById(target);
          if (panel) panel.classList.add('active');
        });
      });
    });
  }

  // =========== 启动 ===========
  function init() {
    renderBottomNav();
    setupBiliVideos();
    setupSubtabs('body');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // =========== 暴露 API ===========
  global.App = {
    toast: toast,
    renderWeightChart: renderWeightChart,
    renderWeightProgress: renderWeightProgress,
    renderTimeline: renderTimeline,
    renderMoves: renderMoves,
    PAGE: PAGE
  };
})(window);
