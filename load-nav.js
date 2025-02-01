document.addEventListener('DOMContentLoaded', function() {
    fetch('/navigation.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('navigation-placeholder').innerHTML = data;
            
            // Highlight current page in navigation
            const currentPath = window.location.pathname;
            const navLinks = document.querySelectorAll('#navigation-placeholder a');
            navLinks.forEach(link => {
                if (link.getAttribute('href') === currentPath) {
                    link.classList.add('active');
                }
            });
        });
});