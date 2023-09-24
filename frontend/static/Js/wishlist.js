import config from './config.js';

const baseUrl = config.baseUrl;
let accessToken = localStorage.getItem('accessToken')

function removeItemFromWishlist(wishlistItemId) {
    fetch(`${baseUrl}/api/wishlist/${wishlistItemId}/`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${accessToken}`,
        },
    })
        .then(response => {
            if (response.status === 204) {
                const wishlistItemCard = document.querySelector(`[data-wishlist-id="${wishlistItemId}"]`);
                if (wishlistItemCard) {
                    wishlistItemCard.parentNode.removeChild(wishlistItemCard);
                }
                displayAlert("Item removed from the wishlist.", "success");
            } else {
                displayAlert("Failed to remove item from the wishlist.", "danger");
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function loadWishlistItems() {
    fetch(`${baseUrl}/api/wishlist/`, {
        headers: {
            'Authorization': `Bearer ${accessToken}`,
        },
    })
        .then(response => response.json())
        .then(data => {
            wishlistContainer.innerHTML = "";

            if (data.length === 0) {
                const emptyWishlistMessage = document.createElement("h2");
                emptyWishlistMessage.textContent = "Your wishlist is empty!";
                wishlistContainer.appendChild(emptyWishlistMessage);
            } else {
                let row = null;
                data.forEach((wishlistItem, index) => {
                    if (index % 4 === 0) {
                        row = document.createElement("div");
                        row.classList.add("row");
                        row.classList.add("mb-3");
                        wishlistContainer.appendChild(row);
                    }

                    const wishlistCard = createWishlistCard(wishlistItem);
                    row.appendChild(wishlistCard);
                });
            }
        })
        .catch(error => {
            console.error("Error fetching wishlist data: ", error);
        });
}

function createWishlistCard(wishlistItem) {
    const wishlistCard = document.createElement("div");
    wishlistCard.classList.add("col-md-3");

    wishlistCard.innerHTML = `
        <div class="card">
            <div class="card-body">
                <h5 class="card-title list-group-item list-group-item-primary">${wishlistItem.product.name}</h5>
            </div>
            <ul class="list-group list-group-flush">
                <li class="card-color list-group-item">Color: ${wishlistItem.product.color}</li>
                <li class="card-price list-group-item">Brand: ${wishlistItem.product.brand}</li>
            </ul>
            <button class="delete-item text-center" data-wishlist-id="${wishlistItem.id}">
                <i class="fa-solid fa-trash"></i>
            </button>
        </div>
    `;

    const deleteButton = wishlistCard.querySelector(".delete-item");
    deleteButton.addEventListener("click", () => {
        const wishlistItemId = deleteButton.getAttribute("data-wishlist-id");
        removeItemFromWishlist(wishlistItemId);
    });

    return wishlistCard;
}

loadWishlistItems();

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
