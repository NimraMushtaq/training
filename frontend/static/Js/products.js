import config from './config.js';

const baseUrl = config.baseUrl;
let accessToken = localStorage.getItem('accessToken')

document.addEventListener("DOMContentLoaded", function () {

    const productContainer = document.getElementById("product-container");
    const colorInput = document.getElementById("color");
    const brandInput = document.getElementById("brand");
    const filterButton = document.getElementById("filter-button");

    function clearInputFields() {
        colorInput.value = "";
        brandInput.value = "";
    }

    // Function to load all products
    function loadAllProducts() {
        fetch(`${baseUrl}/api/products/`)
            .then(response => response.json())
            .then(data => {
                productContainer.innerHTML = "";
                let row = null;
                data.forEach((product, index) => {
                    if (index % 3 === 0) {
                        row = document.createElement("div");
                        row.classList.add("row");
                        row.classList.add("mb-3");
                        productContainer.appendChild(row);
                    }

                    const productCard = createProductCard(product);
                    row.appendChild(productCard);
                });
            })
            .catch(error => {
                console.error("Error fetching data: ", error);
            });
    }

    function createProductCard(product) {
        const productCard = document.createElement("div");
        productCard.classList.add("col");

        productCard.innerHTML = `
        <div class="card" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">${product.name}</h5>
                    <ul class="list-group list-group-flush">
                        <li class="card-color list-group-item">Color: ${product.color}</li>
                        <li class="card-price list-group-item">Brand: ${product.brand}</li>
                    </ul>
             </div>
             <button class="add-to-wishlist" data-product-id="${product.id}">
                <i class="fa-regular fa-heart heart-icon"></i>
             </button>
        </div>
    `;

        productCard.querySelector(".card-body").addEventListener("click", () => {
            fetch(`${baseUrl}/api/products/${product.id}/`)
                .then(response => response.json())
                .then(data => {
                    window.location.href = `product_details.html?id=${product.id}`;
                })
                .catch(error => {
                    console.error("Error fetching product details: ", error);
                });
        });

        // event listener to the heart icon button
        const heartIconBtn = productCard.querySelector(".add-to-wishlist");
        heartIconBtn.addEventListener("click", function () {
            const heartIcon = this.querySelector(".heart-icon");
            const productId = this.dataset.productId;
            if (!heartIcon.classList.contains("red-heart")) {
                // Heart icon is white, add to wishlist
                fetch(`${baseUrl}/api/wishlist/`, {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ product_id: productId }),
                })
                    .then(response => {
                        if (response.status === 201) {
                            heartIcon.classList.add("red-heart");
                            heartIconBtn.innerHTML = `<i class="fa-solid fa-heart" style="color: #cc0000;"></i>`
                            displayAlert("Product added to the wishlist.", "success");
                        } else if (response.status === 200) {
                            displayAlert("Product is already in the wishlist.", "warning");
                        } else {
                            displayAlert("Failed to add product to the wishlist.", "danger");
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
            }
        });



        return productCard;
    }

    // Function to filter products
    function filterProducts() {
        const color = colorInput.value;
        const brand = brandInput.value;

        fetch(`${baseUrl}/api/products/?color=${color}&brand=${brand}`)
            .then(response => response.json())
            .then(data => {
                productContainer.innerHTML = "";

                let row = null;
                data.forEach((product, index) => {
                    if (index % 3 === 0) {
                        row = document.createElement("div");
                        row.classList.add("row");
                        row.classList.add("mb-3");
                        productContainer.appendChild(row);
                    }

                    const productCard = createProductCard(product);
                    row.appendChild(productCard);
                });
            })
            .catch(error => {
                console.error("Error fetching data: ", error);
            });
        clearInputFields();
    }

    loadAllProducts();

    filterButton.addEventListener("click", filterProducts);


    function displayAlert(message, alertType) {

        const alertElement = document.createElement("div");
        alertElement.classList.add("alert", `alert-${alertType}`);
        alertElement.textContent = message;
        const alertContainer = document.getElementById("alert-container");
        alertContainer.appendChild(alertElement);
        setTimeout(() => {
            alertElement.remove();
        }, 3000);
    }

});
