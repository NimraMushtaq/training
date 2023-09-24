import config from './config.js';

const baseUrl = config.baseUrl;

function getProductIdFromQuery() {
    const params = new URLSearchParams(window.location.search);
    return params.get("id");
}
function fetchProductDetails(productId) {
    fetch(`${baseUrl}/api/products/${productId}/`)
        .then(response => response.json())
        .then(product => {

            document.getElementById("productName").textContent = product.name;
            document.getElementById("productColor").textContent = product.color;
            document.getElementById("productBrand").textContent = product.brand;

        })
        .catch(error => {
            console.error("Error fetching product details: ", error);
        });
}

const productId = getProductIdFromQuery();
fetchProductDetails(productId);
