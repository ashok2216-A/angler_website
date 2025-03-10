document.addEventListener('DOMContentLoaded', () => {
  const themeToggleBtn = document.querySelector('.theme-toggle');
  const body = document.body;

  // Debugging: log initial state
  console.log('Initial body class:', body.className);

  themeToggleBtn.addEventListener('click', () => {
    // Toggle between themes
    if (body.classList.contains('light-theme')) {
      body.classList.replace('light-theme', 'dark-theme');
      themeToggleBtn.textContent = "Switch to Light Theme";
      console.log('Switched to dark-theme');
    } else {
      body.classList.replace('dark-theme', 'light-theme');
      themeToggleBtn.textContent = "Switch to Dark Theme";
      console.log('Switched to light-theme');
    }
    console.log('Current body class:', body.className);
  });
});