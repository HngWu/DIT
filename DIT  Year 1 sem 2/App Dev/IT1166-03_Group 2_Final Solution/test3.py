import shelve


def print_order_data():
    # Open the orders_shelf.db file
    with shelve.open("orders_shelf.db", writeback=True) as order_shelf:
        # Check if "allOrders" key exists in the shelf
        if "allOrders" in order_shelf:
            all_orders = order_shelf["allOrders"]

            # Iterate through all orders and print the data
            for order_id, order in all_orders.items():
                print(f"Order ID: {order_id}")
                print(f"Cart: {order.particulars.__str__()}")
                print(f"Cart: {order.cart.show_cart()}")
                for item in order.cart.products:
                    print(item)
                # Print items in the cart



                print("\n------------------------------------\n")

        else:
            print("No orders found in the database.")


if __name__ == "__main__":
    print_order_data()
