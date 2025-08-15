document.addEventListener('DOMContentLoaded', function () {
  var el = document.querySelector('.masthead .site-title, .site-header .site-title');
  if (el) {
    el.setAttribute('href', 'https://www.mydae.org/');
    el.setAttribute('target', '_blank');
    el.setAttribute('rel', 'noopener');
  }
});
