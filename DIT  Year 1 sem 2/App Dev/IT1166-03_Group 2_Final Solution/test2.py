<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Shopping Cart</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .cart-container {
            max-width: 800px;
            margin: 0 auto;
        }

        .product-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 16px;
            margin: 16px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .product-details {
            flex-grow: 1;
            margin-right: 16px;
        }

        .product-image {
            max-width: 100px;
            max-height: 100px;
            border-radius: 8px;
            margin-right: 16px;
        }

        .quantity-controls {
            display: flex;
            align-items: center;
        }

        .quantity-btn {
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1em;
            width: 24px;
            height: 24px;
            margin: 0 4px;
        }

        .quantity-input {
            width: 50px;
            text-align: center;
            font-size: 1em;
            -webkit-appearance: none;
            appearance: none;
        }

        .quantity-input:hover, .quantity-input:focus {
            /* Remove up and down arrows */
            appearance: none;
            -moz-appearance: textfield;
            width: 50px;
        }

        input[type=number]::-webkit-inner-spin-button,
        input[type=number]::-webkit-outer-spin-button {
            -webkit-appearance: none;
            appearance: none;
        }

        .remove-btn {
            color: red;
            cursor: pointer;
            text-align: left;
            display: block;
            margin-top: 8px;
            margin-left: 28px;
        }

        .price {
            text-align: right;
            font-weight: bold;
            font-size: 1.2em;
        }

        .checkout-link {
            text-decoration: none;
            font-weight: bold;
        }
             body {
        padding-top: 56px; /* Adjust based on the height of your navigation bar */
    }

    .navbar {
        background-color: #007bff;
    }

    .navbar-brand {
        color: white;
        font-size: 24px;
        font-weight: bold;
    }

    .navbar-nav {
        margin-left: auto;
    }

    .nav-link {
        color: white;
        margin-right: 15px;
    }

    .search-icon, .cart-icon, .profile-icon {
        color: white;
        font-size: 20px;
        margin-right: 15px;
        cursor: pointer;
    }
    /* Add this to your existing styles or update accordingly */

.subtotal {
    text-align: right;
    margin-top: 20px;
}

.checkout-buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}

.continue-shopping,
.checkout-link {
    padding: 10px 20px;
    text-decoration: none;
    font-weight: bold;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}

.continue-shopping {
    background-color: #007bff;
    color: #fff;
}

.checkout-link {
    background-color: #28a745;
    color: #fff;
}

.continue-shopping:hover,
.checkout-link:hover {
color: white
}
h1, .centertext{
    text-align: center;
}
/* Adjust the colors and styles as needed */

    </style>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
          crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css"
          integrity="sha384-csZXEAg5MhqLMpG8r+Knujsl5+z0I5t9z5lFf5r+brL4Zcv/dpGp1it16IdMK4t6"
          crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark fixed-top bg-primary">
    <a class="navbar-brand" href="{{ url_for('home') }}">NeoType</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mx-auto">
            <li class="nav-item">
                <a class="nav-link" href="#">Keyboards</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Keycaps</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Switches</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Accessories</a>
            </li>
        </ul>
        <div class="d-flex">
            <!-- Add your search icon, cart icon, and profile icon here -->
            <span class="search-icon">&#128269;</span>
            <a href="{{ url_for('view_cart') }}"><span class="cart-icon">&#128722;</span></a>
            <span class="profile-icon">&#128100;</span>
        </div>
    </div>
</nav>

    <!-- Updated view_cart.html -->

<div class="cart-container">
    <h1>Shopping Cart</h1>
    {% if cart.products %}
        {% for product, quantity in cart.products.items() %}
            <div class="product-card">
                <img src="{{ url_for('static', filename=product.get_product_thumbnail()) }}" alt="Product Image" class="product-image">
                <div class="product-details">
                    <h3>{{ product.get_product_name() }}</h3>
                    <p>{{ product.get_product_detail() }}</p>
                    <div class="quantity-controls">
                        <button class="quantity-btn" onclick="adjustQuantity('{{ product.get_product_name() }}', -1)">-</button>
                        <input type="number" inputmode="numeric" id="quantity_{{ product.get_product_name() }}" name="quantity" value="{{ quantity }}" class="quantity-input" min="1">
                        <button class="quantity-btn" onclick="adjustQuantity('{{ product.get_product_name() }}', 1)">+</button>
                    </div>
                    <div class="remove-btn" onclick="deleteProduct('{{ product.get_product_name() }}')">Remove</div>
                </div>
                <div class="price">${{ product.get_product_price() * quantity }}0</div>
            </div>
        {% endfor %}

        <!-- Subtotal calculation and checkout button -->
        <div class="subtotal">
            <p>Subtotal: ${{ cart.calculate_total() }}0</p>
            <a href="{{ url_for('home') }}" class="continue-shopping">Continue Shopping</a>
            <a href="{{ url_for('input_particulars') }}" class="checkout-link">Proceed to Checkout</a>
        </div>

    {% else %}
        <p class="centertext">Your cart is empty.</p>
    {% endif %}
</div>


    <script>
       function adjustQuantity(productName, change) {
        var quantityInput = document.getElementById('quantity_' + productName);
        var newQuantity = parseInt(quantityInput.value) + change;

        // Ensure the quantity doesn't go below 1
        newQuantity = newQuantity < 1 ? 1 : newQuantity;

        // Update the quantity input
        quantityInput.value = newQuantity;

        // Update the price based on the new quantity
        var productPrice = parseFloat(document.getElementById('price_' + productName).innerText.substring(1));
        var newPrice = newQuantity * productPrice;
        document.getElementById('price_' + productName).innerText = '$' + newPrice.toFixed(2);

        // Update the subtotal
        updateSubtotal();
    }

    function deleteProduct(productName) {
        // Implement the logic to delete the product from the cart using JavaScript
        var productCard = document.querySelector('.product-card');

        // Remove the product card from the view
        productCard.remove();

        // Update the subtotal
        updateSubtotal();
    }

    function updateSubtotal() {
        var subtotalElement = document.getElementById('subtotal');
        var subtotal = 0;

        // Calculate the new subtotal based on the prices and quantities of products
        var productCards = document.querySelectorAll('.product-card');
        productCards.forEach(function (card) {
            var productPrice = parseFloat(card.querySelector('.price').innerText.substring(1));
            var quantity = parseInt(card.querySelector('.quantity-input').value);
            subtotal += productPrice * quantity;
        });

        // Update the subtotal element
        subtotalElement.innerText = 'Subtotal: $' + subtotal.toFixed(2);
    }
    </script>
</body>
</html>