from Classes import *
import shelve, uuid




# Load catalog from database
catalog = load_catalog_from_database()
cart = ShoppingCart()
allOrders = load_orders_from_database()


def add_product_to_catalog():
    product_type = input(
        "Enter product type (keyboard, keycaps, switches, accessories): "
    )
    id = int(input("Enter product ID: "))
    sku = input("Enter SKU: ")
    name = input("Enter product name: ")
    detail = input("Enter product detail: ")
    price = float(input("Enter product price: "))
    thumbnail = input("Enter thumbnail filename: ")
    images = input("Enter images filenames separated by commas: ").split(",")
    more_detailed_images = input(
        "Enter more detailed images filenames separated by commas: "
    ).split(",")

    if product_type == "keyboard":
        switch = input("Enter switch type: ")
        product = Keyboard(
            id,
            sku,
            name,
            detail,
            price,
            thumbnail,
            images,
            more_detailed_images,
            switch,
        )
    elif product_type == "keycaps":
        product = KeyCaps(
            id, sku, name, detail, price, thumbnail, images, more_detailed_images
        )
    elif product_type == "switches":
        product = Switches(
            id, sku, name, detail, price, thumbnail, images, more_detailed_images
        )
    elif product_type == "accessories":
        product = Accessories(
            id, sku, name, detail, price, thumbnail, images, more_detailed_images
        )
    else:
        print("Invalid product type.")
        return

    catalog[sku] = product

    print(f"{product_type.capitalize()} added to catalog successfully.")
    with shelve.open("catalog_shelf.db") as shelf:
        shelf["catalog"] = catalog


def display_menu():
    while True:
        print("Select the program (1-9) to run: ")
        print("1. View Product Details")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. View Particulars")
        print("6. Add review")
        print("7. Show review")
        print("8. Add Product to Catalog")
        print("9. End Program")
        val = int(input("Enter your command (1-9): "))
        if val == 9:
            print("End of program")
            break
        elif val == 1:
            view_product_details()
        elif val == 2:
            add_to_cart()
        elif val == 3:
            view_cart()
        elif val == 4:
            checkout()
        elif val == 5:
            view_particulars()
        elif val == 6:
            add_review()
        elif val == 7:
            view_product_reviews()
        elif val == 8:
            add_product_to_catalog()


def view_product_details():
    product_name = input(
        "What product would you like to view? (keyboard, keycaps, switches, accessories): "
    )
    # Use SKU instead of product name in the condition
    for sku, product in catalog.items():
        if product.get_name().lower() == product_name.lower():
            print(product.__str__())
            return
    else:
        print("Product not found in catalog.")



def add_to_cart():
    product_name = input(
        "What product would you like to add? (keyboard, keycaps, switches, accessories): "
    )
    quantity = input("What quantity would you like to add? ")
    # Use SKU instead of product name in the condition
    for sku, product in catalog.items():
        if product.get_name().lower() == product_name.lower():
            cart.add_product(product, quantity)
            print("Product added to cart successfully.")
            return
    else:
        print("Product not found in catalog.")


def add_review():
    user = input("Input Name: ")
    product_name = input("Input Name of Product: ")
    rating = input("Input Rating: ")
    comment = input("Input Comment: ")
    # Use SKU instead of product name in the condition
    for sku, product in catalog.items():
        if product.get_name().lower() == product_name.lower():
            product.add_review(user, rating, comment)
            print("Review added successfully.")
            return
    else:
        print("Product not found in catalog.")


def view_product_reviews():
    product_name = input("Input Name of Product: ")
    # Use SKU instead of product name in the condition
    for sku, product in catalog.items():
        if product.get_name().lower() == product_name.lower():
            reviews = product.get_reviews()
            if reviews:
                print("Product Reviews:")
                for review in reviews:
                    print(
                        f"User: {review['user']}, Rating: {review['rating']}, Comment: {review['comment']}"
                    )
            else:
                print("No reviews available for this product.")
            return
    else:
        print("Product not found in catalog.")



def view_cart():
    print("Shopping Cart:")
    for item, quantity in cart.products.items():
        print(f"Item: {item.get_name()}, Quantity: {quantity}")


def checkout():
    if not cart.products:
        print("Cart is empty. Add products before checking out.")
        return

    # Generate a unique order number using UUID
    order_number = str(uuid.uuid4())

    address = input("Enter Address: ")
    postalcode = input("Enter Postal Code: ")
    shipping = input("Enter Shipping Method: ")
    particulars = Particulars(address, postalcode, shipping)

    # Create an order and add it to the database
    order = Order(order_number, cart, particulars)
    allOrders[order_number] = order

    # Clear the cart after successful checkout
    cart.products.clear()

    print("Order placed successfully. Order number:", order_number)

    # Update the orders database
    with shelve.open("orders_shelf.db") as order_shelf:
        order_shelf["allOrders"] = allOrders


def view_all_orders():
    if not allOrders:
        print("No orders found.")
        return

    print("All Orders:")
    for order_number, order in allOrders.items():
        print("\nOrder Number:", order_number)
        print("Shopping Cart:")
        for item, quantity in order.cart.products.items():
            print(f"Item: {item.get_name()}, Quantity: {quantity}")
        print("Particulars:")
        print(order.particulars)

def view_particulars():
    view_all_orders()




# Call the main menu function
display_menu()
