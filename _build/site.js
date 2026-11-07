(function () {
  // Email is assembled here so bots reading the raw HTML don't see a plain address.
  document.querySelectorAll(".js-email").forEach(function (a) {
    var addr = a.dataset.u + "@" + a.dataset.d;
    a.href = "mailto:" + addr;
    a.textContent = addr;
  });

  // ---------- READ meter in the top bar: fills as the page scrolls ----------
  var cellsEl = document.querySelector(".read-cells"), pctEl = document.querySelector(".read-pct");
  if (cellsEl && pctEl) {
    for (var c = 0; c < 12; c++) cellsEl.appendChild(document.createElement("i"));
    var cells = cellsEl.querySelectorAll("i");
    var update = function () {
      var max = document.documentElement.scrollHeight - window.innerHeight;
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

  var sleep = function (ms) { return new Promise(function (r) { setTimeout(r, ms); }); };

  // ---------- Home: profile window types its labels, then shows each value ----------
  var con = document.querySelector("[data-console]");
  if (con && !reduce) {
    con.classList.add("is-typing");
    var steps = Array.prototype.slice.call(con.querySelectorAll(".window-body > *"));
    (async function () {
      await sleep(250);
      for (var s = 0; s < steps.length; s++) {
        var el = steps[s], t = el.querySelector(".hud-text");
        if (t) {
          var full = t.textContent;
          t.textContent = "";
          el.classList.add("shown");
          t.classList.add("shown");
          for (var k = 1; k <= full.length; k++) { t.textContent = full.slice(0, k); await sleep(45); }
          await sleep(160);
        } else {
          el.classList.add("shown");
          await sleep(220);
        }
      }
      con.classList.remove("is-typing");
    })();
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
    filters.forEach(function (btn) {
      btn.addEventListener("click", function () {
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
      });
    });
  }

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
  function showOptions() {
    opts.innerHTML = "";
    data.topics.forEach(function (t, i) {
      if (asked[i]) return;
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "chat-opt";
      btn.textContent = t.q;
      btn.addEventListener("click", function () { ask(i); });
      opts.appendChild(btn);
    });
    var a = document.createElement("a");
    a.className = "chat-opt final";
    a.href = data.finalHref;
    a.textContent = data.final;
    opts.appendChild(a);
  }

  async function ask(i) {
    asked[i] = true;
    opts.innerHTML = "";
    bubble("me", data.topics[i].q);
    await wait(160);
    await natSays(data.topics[i].a);
    showOptions();
  }

  (async function start() {
    await wait(120);
    await natSays(data.intro);
    showOptions();
    scrollDown();
  })();
})();
