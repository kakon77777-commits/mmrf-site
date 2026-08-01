// Three small behaviours. The site is fully readable without any of them.
(function () {
  "use strict";

  // Colour scheme. The boot script in <head> has already applied any stored
  // preference; this only handles the toggle and remembering the choice.
  var root = document.documentElement;
  function current() {
    var set = root.getAttribute("data-theme");
    if (set) return set;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  Array.prototype.forEach.call(
    document.querySelectorAll("[data-theme-toggle]"),
    function (button) {
      button.addEventListener("click", function () {
        var next = current() === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", next);
        try { localStorage.setItem("mmrf-theme", next); } catch (e) {}
      });
    }
  );

  // Copy the citation. Falls back to a selection the reader can copy by hand
  // if the clipboard API is unavailable or refused.
  Array.prototype.forEach.call(
    document.querySelectorAll("[data-copy]"),
    function (button) {
      button.addEventListener("click", function () {
        var text = button.getAttribute("data-copy");
        var done = button.getAttribute("data-copied") || "Copied";
        var label = button.textContent;
        function ok() {
          button.textContent = done;
          setTimeout(function () { button.textContent = label; }, 1600);
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(ok, select);
        } else {
          select();
        }
        function select() {
          var quote = button.parentNode.querySelector(".cite-q");
          if (!quote || !window.getSelection) return;
          var range = document.createRange();
          range.selectNodeContents(quote);
          var sel = window.getSelection();
          sel.removeAllRanges();
          sel.addRange(range);
        }
      });
    }
  );

  // Mark the section currently in view in the table of contents.
  var links = document.querySelectorAll("[data-toc-link]");
  if (!links.length || !window.IntersectionObserver) return;
  var byId = {};
  Array.prototype.forEach.call(links, function (link) {
    byId[link.getAttribute("href").slice(1)] = link;
  });
  var seen = {};
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      seen[entry.target.id] = entry.isIntersecting;
    });
    var active = null;
    Object.keys(byId).forEach(function (id) {
      if (seen[id] && !active) active = id;
    });
    Array.prototype.forEach.call(links, function (link) {
      link.classList.toggle("on", link.getAttribute("href") === "#" + active);
    });
  }, { rootMargin: "-72px 0px -70% 0px" });
  Object.keys(byId).forEach(function (id) {
    var heading = document.getElementById(id);
    if (heading) observer.observe(heading);
  });
})();
