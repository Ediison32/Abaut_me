
const toggleTheme = document.getElementById('theme-toggle');
const body = document.body;

toggleTheme.addEventListener('click', () => {
    body.classList.toggle('dark');
    const icon = toggleTheme.querySelector('i');
    icon.classList.toggle('fa-moon');
    icon.classList.toggle('fa-sun');
});