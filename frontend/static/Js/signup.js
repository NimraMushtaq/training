import config from './config.js';

const baseUrl = config.baseUrl;

document.addEventListener("DOMContentLoaded", function () {
    const signupForm = document.getElementById("signup-form");

    signupForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const firstName = document.getElementById("InputLastName").value;
        const lastName = document.getElementById("inputFirstName").value;
        const email = document.getElementById("inputEmail").value;
        const password = document.getElementById("inputPassword").value;

        const user = {
            first_name: firstName,
            last_name: lastName,
            email: email,
            password: password,
        };

        fetch(`${baseUrl}/api/auth/register/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(user),
        })
            .then(response => {
                if (response.ok) {
                    alert('Signup successful');
                    signupForm.reset();
                    window.location.href = "login.html";
                } else {
                    return response.text().then(errorMessage => {
                        try {
                            const errorData = JSON.parse(errorMessage);
                            if (Array.isArray(errorData) && errorData.length > 0) {
                                const firstErrorMessage = errorData[0];
                                alert(`Signup failed: ${firstErrorMessage}`);
                            } else {
                                alert('Signup failed');
                            }
                        } catch (jsonError) {
                            alert('Signup failed. An error occurred.');
                        }
                    });
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });



    });
});
