import config from './config.js';

const baseUrl = config.baseUrl;
function logout() {
    const logoutUrl = `${baseUrl}/api/logout/`;

    const accessToken = localStorage.getItem('accessToken'); 
    if (accessToken) {
        fetch(logoutUrl, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${accessToken}`,
                'Content-Type': 'application/json',
            },
        })
            .then(response => {
                return response.json();
            })
            .then(data => {
                console.log('Response data:', data);
                if (data.message) {
                    localStorage.removeItem('accessToken');
                    localStorage.removeItem('refreshToken'); 
                    localStorage.removeItem('auth');

                    window.location.href = 'login.html';
                } else {
                    console.error('Logout failed:', data.message);
                }
            })
            .catch(error => {
                console.error('Error during logout:', error);
            });
    }
}
export { logout };
