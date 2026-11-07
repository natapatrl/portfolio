(function () {
  // Email is assembled here so bots reading the raw HTML don't see a plain address.
  document.querySelectorAll(".js-email").forEach(function (a) {
    var addr = a.dataset.u + "@" + a.dataset.d;
    a.href = "mailto:" + addr;
    a.textContent = addr;
  });

  // ---------- About page: texting game ----------
  var chat = document.querySelector("[data-chat]");
  var dataEl = document.getElementById("chat-data");
  if (!chat || !dataEl) return;

  var data = JSON.parse(dataEl.textContent);
  var log = chat.querySelector(".chat-log");
  var opts = chat.querySelector(".chat-options");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
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
      await wait(500 + Math.min(lines[i].length * 14, 1100));
      typing(false);
      bubble("them", lines[i]);
      await wait(250);
    }
  }

  function showOptions() {
    opts.innerHTML = "";
    var left = data.topics.filter(function (t, i) { return !asked[i]; });
    if (!left.length) {
      var a = document.createElement("a");
      a.className = "chat-opt final";
      a.href = data.finalHref;
      a.textContent = data.final;
      opts.appendChild(a);
      return;
    }
    data.topics.forEach(function (t, i) {
      if (asked[i]) return;
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "chat-opt";
      btn.textContent = t.q;
      btn.addEventListener("click", function () { ask(i); });
      opts.appendChild(btn);
    });
  }

  async function ask(i) {
    asked[i] = true;
    opts.innerHTML = "";
    bubble("me", data.topics[i].q);
    await wait(350);
    await natSays(data.topics[i].a);
    showOptions();
  }

  (async function start() {
    await wait(300);
    await natSays(data.intro);
    showOptions();
    scrollDown();
  })();
})();
