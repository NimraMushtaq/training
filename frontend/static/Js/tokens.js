import config from './config.js';

const baseUrl = config.baseUrl;
let refreshToken = localStorage.getItem('refreshToken') || '';
let accessToken = localStorage.getItem('accessToken') || '';

function refreshAccessToken(callback) {
    const tokenUrl = `${baseUrl}/api/token/refresh/`;
    const requestData = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refresh: refreshToken }),
    };

    fetch(tokenUrl, requestData)
        .then((response) => {
            if (response.status === 200) {
                return response.json();
            } else {
                throw new Error('Token refresh failed');
            }
        })
        .then((data) => {
            accessToken = data.access;
            localStorage.setItem('accessToken', accessToken);
            localStorage.setItem('auth', true);

            if (typeof callback === 'function') {
                callback(accessToken);
            }
        })
        .catch((error) => {
            console.error('Token refresh error:', error);
        });
}

function verifyAccessToken() {
    const tokenUrl = `${baseUrl}/api/token/verify/`;
    const requestData = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ token: accessToken }),
    };

    return fetch(tokenUrl, requestData)
        .then((response) => {
            if (response.status === 200) {
                localStorage.setItem('auth', true);
                return true;
            } else if (response.status === 401) {
                localStorage.setItem('auth', false);
                return false;
            } else {
                throw new Error('Token verification failed');
            }
        })
        .catch((error) => {
            console.error('Token verification error:', error);
            return false;
        });
}


window.addEventListener('load', handleTokenExpiration);

async function handleTokenExpiration() {

    const isAccessTokenExpired = await verifyAccessToken();

    if (isAccessTokenExpired) {
        return;
    }

    try {
        const newAccessToken = await refreshAccessToken();
        localStorage.setItem('accessToken', newAccessToken);
    } catch (error) {
        console.error('Error refreshing token:', error);
    }
}

setInterval(handleTokenExpiration, 6000);
export { verifyAccessToken } 
