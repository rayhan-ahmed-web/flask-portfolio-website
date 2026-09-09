const menuToggle = document.querySelector('.menu-toggle');
const navMenu = document.querySelector('#nav-menu');

if (menuToggle && navMenu) {
    menuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('open');
        menuToggle.setAttribute('aria-expanded', navMenu.classList.contains('open'));
    });

    navMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => navMenu.classList.remove('open'));
    });
}

// Prevent accidental duplicate form submission while the request is processing.
const form = document.querySelector('.contact-form');
if (form) {
    form.addEventListener('submit', () => {
        const button = form.querySelector('button[type="submit"]');
        if (button) {
            button.disabled = true;
            button.textContent = 'Sending...';
        }
    });
}
