import { logout } from './logout.js';

function loadNavbarAndUpdateLinks() {
    const navbarContainer = document.getElementById('navbarContainer');
    if (navbarContainer) {

        fetch('navbar.html') 
            .then(response => response.text())
            .then(navbarHTML => {
                navbarContainer.innerHTML = navbarHTML;
                
                    let isAuthenticated = localStorage.getItem('auth') === 'true'; 
                        const loginLink = document.getElementById('loginLink');
                        const signupLink = document.getElementById('signupLink');
                        const wishlistLink = document.getElementById('wishlistLink');
                        const signoutLink = document.getElementById('signoutLink');

                        if (isAuthenticated) {
                            loginLink.style.display = 'none';
                            signupLink.style.display = 'none';
                        } else {
                            wishlistLink.style.display = 'none';
                            signoutLink.style.display = 'none';
                        }
                        signoutLink.addEventListener('click', (e) => {
                            e.preventDefault();
                            logout(); 
                        });
                    });
    }
}

window.addEventListener('load', loadNavbarAndUpdateLinks);
