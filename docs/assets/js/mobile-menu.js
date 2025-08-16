
document.addEventListener('DOMContentLoaded', function () {
  const nav = document.querySelector('.site-header .greedy-nav, .masthead .greedy-nav');
  if (!nav) return;
  let btn = nav.querySelector('.greedy-nav__toggle');
  if (!btn) {
    btn = document.createElement('button');
    btn.className = 'greedy-nav__toggle';
    btn.setAttribute('aria-label', 'Toggle navigation');
    btn.innerHTML = '<span aria-hidden="true">&#9776;</span>';
    nav.appendChild(btn);
  } else {
    btn.classList.remove('hidden');
  }
  function closeMenu(){ nav.classList.remove('is-open'); btn.setAttribute('aria-expanded','false'); }
  btn.setAttribute('aria-expanded','false');
  btn.addEventListener('click', function(){ const open = nav.classList.toggle('is-open'); btn.setAttribute('aria-expanded', open ? 'true':'false'); });
  nav.querySelectorAll('.visible-links a').forEach(a => a.addEventListener('click', closeMenu));
  document.addEventListener('click', e => { if (!nav.contains(e.target)) closeMenu(); });
});
