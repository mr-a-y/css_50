(() => {
  const html = document.documentElement;
  const mq = window.matchMedia('(prefers-color-scheme: dark)');

  const stored = localStorage.getItem('theme'); 
  if (!stored) applyTheme(mq.matches ? 'dark' : 'light');

  mq.addEventListener('change', (e) => {
    if (!localStorage.getItem('theme')) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });


  document.addEventListener('click', (e) => {
    const btn = e.target.closest('#theme-toggle');
    if (!btn) return;
    const current = html.getAttribute('data-bs-theme') === 'dark' ? 'dark' : 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', next);
    applyTheme(next);
  });

  function applyTheme(t) {
    html.setAttribute('data-bs-theme', t);
    const icon = document.getElementById('theme-toggle-icon');
    if (icon) icon.textContent = t === 'dark' ? '☀️' : '🌙'; 
  }
})();
