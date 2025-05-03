function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
  
 
  document.body.classList.add('dark-mode-transition');
  window.setTimeout(() => {
    document.body.classList.remove('dark-mode-transition');
  }, 500);
}
