
document.addEventListener('DOMContentLoaded', function () {
  // Build the component
  const wrap = document.createElement('div');
  wrap.className = 'follow-dropdown follow-placement';
  wrap.innerHTML = `
    <button type="button" id="followBtn" class="follow-btn" aria-haspopup="true" aria-expanded="false" aria-controls="followMenu">
      Follow
      <svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24" class="caret">
        <path d="M7 10l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2"></path>
      </svg>
    </button>
    <nav id="followMenu" class="follow-menu" role="menu">
      <a role="menuitem" href="https://github.com/jnapfx" target="_blank" rel="noopener">GitHub</a>
      <a role="menuitem" href="https://www.linkedin.com/in/" target="_blank" rel="noopener">LinkedIn</a>
      <a role="menuitem" href="/feed.xml">RSS</a>
    </nav>
  `;

  // Insert near top of main content
  const main = document.querySelector('main') || document.querySelector('.initial-content') || document.body;
  if (main) {
    // Prefer placing after the first H1
    const h1 = main.querySelector('h1');
    if (h1 && h1.parentElement) {
      const holder = document.createElement('div');
      holder.className = 'follow-holder';
      holder.appendChild(wrap);
      h1.parentElement.insertBefore(holder, h1.nextSibling);
    } else {
      main.insertBefore(wrap, main.firstChild);
    }
  } else {
    document.body.appendChild(wrap);
  }

  const btn  = wrap.querySelector('#followBtn');
  const menu = wrap.querySelector('#followMenu');

  if(!btn || !menu) return;

  btn.addEventListener('click', (e)=>{
    e.stopPropagation();
    const open = menu.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  document.addEventListener('click', (e)=>{
    if (!wrap.contains(e.target)){
      menu.classList.remove('open');
      btn.setAttribute('aria-expanded','false');
    }
  });

  document.addEventListener('keydown', (e)=>{
    if(e.key === 'Escape'){
      menu.classList.remove('open');
      btn.setAttribute('aria-expanded','false');
      btn.focus();
    }
  });
});
