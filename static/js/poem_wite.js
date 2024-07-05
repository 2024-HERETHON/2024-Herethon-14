document.addEventListener('DOMContentLoaded', () => {
    const textarea = document.querySelector('.poem-review-input');
    const button = document.querySelector('.poem-review-button');

    textarea.addEventListener('input', () => {
        if (textarea.value.trim() !== '') {
            button.classList.add('enabled');
            button.disabled = false;
        }
        else {
            button.classList.remove('enabled');
            button.disabled = false;
        }
    });

    button.addEventListener('click', () => {
        if (!button.disabled) {
            localStorage.setItem('poemShare', textarea.value.trim());
            window.location.href = 'poem_share.html';
        }
    })
});