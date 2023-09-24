import config from './config.js';

const baseUrl = config.baseUrl;
document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login-form");

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const email = loginForm.elements.email.value;
        const password = loginForm.elements.password.value;

        fetch(`${baseUrl}/api/auth/login/`, {
            method: 'POST',
            body: JSON.stringify({ email, password }),
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then(response => response.json())
            .then(data => {

                if (data.access_token) {
                    localStorage.setItem('accessToken', data.access_token);
                    localStorage.setItem('refreshToken', data.refresh_token);

                    alert('Login successful!');
                    loginForm.reset();
                    window.location.href = "home.html";
                } else {
                    alert('Invalid credentials. Please try again.');
                }
            })
            .catch(error => {
                alert('An error occurred during login.');
            });
    });
});
