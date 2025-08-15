document.addEventListener('DOMContentLoaded', function () {
  const nav = document.querySelector('.site-header .greedy-nav, .masthead .greedy-nav');
  if (!nav) return;

  // Ensure toggle button exists
  let btn = nav.querySelector('.greedy-nav__toggle');
  if (!btn) {
    btn = document.createElement('button');
    btn.className = 'greedy-nav__toggle';
    btn.setAttribute('aria-label', 'Toggle navigation');
    btn.setAttribute('aria-expanded', 'false');
    btn.innerHTML = '<span aria-hidden="true">&#9776;</span>'; // ☰
    nav.appendChild(btn);
  }

  btn.addEventListener('click', function () {
    const open = nav.classList.toggle('is-open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Close menu when a link is clicked (good UX)
  nav.querySelectorAll('.visible-links a').forEach(function (a) {
    a.addEventListener('click', function () {
      nav.classList.remove('is-open');
      btn.setAttribute('aria-expanded', 'false');
    });
  });
});
