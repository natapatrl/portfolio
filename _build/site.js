(function () {
  // Email is assembled here so bots reading the raw HTML don't see a plain address.
  document.querySelectorAll(".js-email").forEach(function (a) {
    var addr = a.dataset.u + "@" + a.dataset.d;
    a.href = "mailto:" + addr;
    a.textContent = addr;
  });

  // ---------- READ meter in the top bar: fills as the page scrolls ----------
  // Hidden on pages too short to scroll (and on phones, in CSS).
  var readEl = document.querySelector(".read");
  var cellsEl = document.querySelector(".read-cells"), pctEl = document.querySelector(".read-pct");
  if (cellsEl && pctEl) {
    for (var c = 0; c < 12; c++) cellsEl.appendChild(document.createElement("i"));
    var cells = cellsEl.querySelectorAll("i");
    var update = function () {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      if (readEl) readEl.classList.toggle("off", max < 40);
      var p = max > 0 ? Math.min(1, window.scrollY / max) : 1;
      var on = Math.round(p * cells.length);
      cells.forEach(function (el, i) { el.classList.toggle("on", i < on); });
      pctEl.textContent = Math.round(p * 100) + "%";
    };
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
  }

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---------- Sticky bars: share their heights with CSS (--hh, --nh) ----------
  var header = document.querySelector(".site-header"), pnav = document.querySelector(".proj-nav");
  var root = document.documentElement;
  var measure = function () {
    if (header) root.style.setProperty("--hh", header.offsetHeight + "px");
    if (pnav) root.style.setProperty("--nh", pnav.offsetHeight + "px");
  };
  measure();
  window.addEventListener("resize", measure);
  if (pnav) {
    // .stuck = the project nav is pinned under the top bar (gives it a solid background)
    var stuckCheck = function () {
      var top = header ? header.offsetHeight : 0;
      pnav.classList.toggle("stuck", window.scrollY > 0 && pnav.getBoundingClientRect().top <= top + 0.5);
    };
    window.addEventListener("scroll", stuckCheck, { passive: true });
    window.addEventListener("resize", stuckCheck);
    stuckCheck();
  }

  // ---------- Home: SCROLL prompt hides once the visitor scrolls (or if there's nothing below) ----------
  var cue = document.querySelector(".scroll-cue");
  if (cue) {
    var cueCheck = function () {
      var room = document.documentElement.scrollHeight - window.innerHeight;
      if (window.scrollY > 40 || room < 80) {
        cue.classList.add("gone");
        window.removeEventListener("scroll", cueCheck);
      }
    };
    window.addEventListener("scroll", cueCheck, { passive: true });
    cueCheck();
  }

  var sleep = function (ms) { return new Promise(function (r) { setTimeout(r, ms); }); };

  // ---------- Home: profile window types its labels, then shows each value ----------
  // Plays once per visit (browser tab); coming back to Home shows everything straight away.
  var con = document.querySelector("[data-console]");
  var introSeen = false;
  try { introSeen = sessionStorage.getItem("introSeen") === "1"; sessionStorage.setItem("introSeen", "1"); } catch (err) {}
  if (con && (reduce || introSeen)) {
    var cur0 = con.querySelector(".cursor");
    if (cur0 && !reduce) cur0.classList.add("go");
  }
  if (con && !reduce && !introSeen) {
    con.classList.add("is-typing");
    var steps = Array.prototype.slice.call(con.querySelectorAll(".window-body > *"));
    (async function () {
      await sleep(150);
      for (var s = 0; s < steps.length; s++) {
        var el = steps[s], t = el.querySelector(".hud-text");
        if (t) {
          var full = t.textContent;
          t.textContent = "";
          el.classList.add("shown");
          t.classList.add("shown");
          for (var k = 1; k <= full.length; k++) { t.textContent = full.slice(0, k); await sleep(30); }
          await sleep(110);
        } else {
          el.classList.add("shown");
          await sleep(150);
        }
      }
      con.classList.remove("is-typing");
      var cur = con.querySelector(".cursor");
      if (cur) cur.classList.add("go");
    })();
  }

  // ---------- Home: "Out now" light flickers on once it's on screen ----------
  var lights = document.querySelectorAll(".badge.b-status");
  if (lights.length) {
    if (reduce || !("IntersectionObserver" in window)) {
      lights.forEach(function (l) { l.classList.add("lit"); });
    } else {
      var lio = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          en.target.classList.add("lit");
          lio.unobserve(en.target);
        });
      }, { threshold: 1 });
      lights.forEach(function (l) { lio.observe(l); });
    }
  }

  // ---------- Home: design quest band rips the page open when it scrolls into view ----------
  var rip = document.querySelector("[data-rip]");
  if (rip && !reduce && "IntersectionObserver" in window) {
    rip.classList.add("rip-ready");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        rip.classList.add("ripped");
        io.disconnect();
        // once done, drop the clip so nothing stays cut off
        setTimeout(function () { rip.classList.remove("rip-ready", "ripped"); }, 1200);
      });
    }, { threshold: 0.6 });
    io.observe(rip);
  }

  // ---------- Projects page: discipline filter ----------
  var filters = document.querySelectorAll(".filter");
  if (filters.length) {
    var rows = document.querySelectorAll(".mission");
    var status = document.querySelector(".filter-status");
    // The chosen filter is kept in the address (#level), so Back from a project and the
    // CLASS chips on Home open the list already filtered.
    var applyFilter = function (btn, remember) {
        var f = btn.dataset.filter, shown = 0;
        filters.forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
        var last = null;
        rows.forEach(function (r) {
          var on = f === "all" || r.dataset.tags.split(" ").indexOf(f) > -1;
          r.hidden = !on;
          r.classList.remove("last-shown");
          if (on) { shown++; last = r; }
        });
        if (last) last.classList.add("last-shown");
        if (status) status.textContent = f === "all" ? "" : "Showing " + shown + " of " + rows.length;
        if (remember) {
          try { history.replaceState(null, "", f === "all" ? location.pathname : "#" + f.replace("t-", "")); } catch (err) {}
        }
    };
    filters.forEach(function (btn) {
      btn.addEventListener("click", function () { applyFilter(btn, true); });
    });
    var fromHash = function () {
      var want = "t-" + location.hash.slice(1);
      filters.forEach(function (b) { if (b.dataset.filter === want) applyFilter(b, false); });
    };
    fromHash();
    window.addEventListener("hashchange", fromHash);
  }

  // ---------- Project pages: DESIGN LOG tabs ----------
  document.querySelectorAll("[data-log]").forEach(function (log) {
    var t = log.querySelectorAll(".dl-tab"), p = log.querySelectorAll(".dl-pane");
    function go(i, focus) {
      if (i < 0 || i >= t.length) return;
      t.forEach(function (x, j) {
        var on = j === i;
        x.setAttribute("aria-selected", on ? "true" : "false");
        x.tabIndex = on ? 0 : -1;
        p[j].classList.toggle("on", on);
      });
      t[i].querySelector(".dl-pip").classList.add("seen");
      if (focus) t[i].focus();
    }
    t.forEach(function (x, i) {
      x.addEventListener("click", function () { go(i); });
      x.addEventListener("keydown", function (e) {
        var k = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: t.length - 1 }[e.key];
        if (k !== undefined) { e.preventDefault(); go(Math.max(0, Math.min(t.length - 1, k)), true); }
      });
    });
    p.forEach(function (pane, i) {
      pane.querySelector(".dl-prev").addEventListener("click", function () { go(i - 1, true); });
      pane.querySelector(".dl-next").addEventListener("click", function () { go(i + 1, true); });
    });
    log.querySelectorAll(".dl-open").forEach(function (b) { b.addEventListener("click", function () { go(+b.dataset.go, true); }); });
    // links from other projects open a specific tab: #log-3
    var m = location.hash.match(/^#log-(\d+)$/);
    if (m) { go(+m[1]); log.scrollIntoView({ block: "start" }); }
  });

  // ---------- About page: texting game ----------
  var chat = document.querySelector("[data-chat]");
  var dataEl = document.getElementById("chat-data");
  if (!chat || !dataEl) return;

  var data = JSON.parse(dataEl.textContent);
  var log = chat.querySelector(".chat-log");
  var opts = chat.querySelector(".chat-options");
  var asked = {};

  log.innerHTML = "";
  opts.innerHTML = "";
  opts.tabIndex = -1;   // focusable by script only, to hold focus while options are rebuilt

  function wait(ms) { return new Promise(function (r) { setTimeout(r, reduce ? 0 : ms); }); }

  function scrollDown() {
    var r = opts.getBoundingClientRect();
    if (r.bottom > window.innerHeight) window.scrollBy({ top: r.bottom - window.innerHeight + 24, behavior: reduce ? "auto" : "smooth" });
  }

  function bubble(side, text) {
    var b = document.createElement("div");
    b.className = "bubble " + side;
    var p = document.createElement("p");
    p.textContent = text;
    b.appendChild(p);
    log.appendChild(b);
    requestAnimationFrame(function () { b.classList.add("shown"); });
    scrollDown();
  }

  function typing(on) {
    var t = log.querySelector(".typing");
    if (on && !t) {
      t = document.createElement("div");
      t.className = "bubble them typing shown";
      t.setAttribute("aria-hidden", "true");
      t.innerHTML = "<span></span><span></span><span></span>";
      log.appendChild(t);
      scrollDown();
    } else if (!on && t) {
      t.remove();
    }
  }

  // Nat "types" each message, with a delay that grows a little with its length.
  async function natSays(lines) {
    for (var i = 0; i < lines.length; i++) {
      typing(true);
      await wait(220 + Math.min(lines[i].length * 5, 480));
      typing(false);
      bubble("them", lines[i]);
      await wait(110);
    }
  }

  // The questions not yet asked, plus "View my projects", which is always offered last.
  // focusFirst: after a keyboard pick, put focus on the first new option, so keyboard and
  // screen reader users stay in the chat instead of being dropped back to the top of the page.
  function showOptions(focusFirst) {
    opts.innerHTML = "";
    data.topics.forEach(function (t, i) {
      if (asked[i]) return;
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "chat-opt";
      btn.textContent = t.q;
      // detail is 0 when the click came from Enter/Space rather than a mouse or tap
      btn.addEventListener("click", function (ev) { ask(i, ev.detail === 0); });
      opts.appendChild(btn);
    });
    var a = document.createElement("a");
    a.className = "chat-opt final";
    a.href = data.finalHref;
    a.textContent = data.final;
    opts.appendChild(a);
    if (focusFirst) opts.firstChild.focus();
  }

  async function ask(i, byKeyboard) {
    asked[i] = true;
    // hold focus on the options group while Nat replies (the button that had it is removed)
    if (byKeyboard) opts.focus();
    opts.innerHTML = "";
    bubble("me", data.topics[i].q);
    await wait(160);
    await natSays(data.topics[i].a);
    showOptions(byKeyboard);
  }

  (async function start() {
    await wait(120);
    await natSays(data.intro);
    showOptions();
    scrollDown();
  })();
})();
