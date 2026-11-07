(function () {
  document.documentElement.classList.add("js");

  // Email is assembled here so bots reading the raw HTML don't see a plain address.
  document.querySelectorAll(".js-email").forEach(function (a) {
    var addr = a.dataset.u + "@" + a.dataset.d;
    a.href = "mailto:" + addr;
    a.textContent = addr;
  });

  // About page: reveal chat bubbles one by one, like messages arriving.
  var bubbles = document.querySelectorAll(".chat .bubble:not(.typing)");
  if (bubbles.length) {
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    bubbles.forEach(function (b, i) {
      setTimeout(function () { b.classList.add("shown"); }, reduce ? 0 : 250 + i * 450);
    });
  }
})();
