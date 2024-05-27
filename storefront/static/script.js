const wrapper = document.querySelector('.wrapper');
const iconClose = document.querySelector('.icon-close');

iconClose.addEventListener('click', () => {
    window.location.href = '/'; 
});

document.addEventListener('DOMContentLoaded', function() {
    const closeBtn = document.getElementById('closeBtn');
    
    if (closeBtn) {
        closeBtn.addEventListener('click', function() {
            window.location.href = '/';
        });
    }
});
