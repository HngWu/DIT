# Import shelve module
import shelve


# Function to load catalog from the database
def load_catalog_from_database():
    productDict = {}
    db = shelve.open('products.db', 'c')
    try:
        if 'Products' in db:
            productDict = db['Products']
        else:
            db['Products'] = productDict
    except:
        print("Error in opening products.db.")


# Function to load orders from the database
def load_orders_from_database():
    try:
        with shelve.open("orders_shelf.db") as shelf:
            return shelf.get("allOrders", {})
    except FileNotFoundError:
        return {}


class Product:
    def __init__(
        self,
        id,
        name,
        sku,
        quantity,
        price,
        status,
        discount,
        detail,
        thumbnail,
        images,
        more_detailed_images,
        type,
    ):
        self.__id = id
        self.__name = name
        self.__sku = sku
        self.__quantity = quantity
        self.__price = price
        self.__status = status
        self.__discount = discount
        self.__detail = detail
        self.__thumbnail = thumbnail
        self.__images = images
        self.__more_detailed_images = more_detailed_images
        self.__type = type
        self.__reviews = []

    def get_product_id(self):
        return self.__id

    def get_product_name(self):
        return self.__name

    def get_product_sku(self):
        return self.__sku

    def get_product_quantity(self):
        return self.__quantity

    def get_product_price(self):
        return self.__price

    def get_product_status(self):
        return self.__status

    def get_product_discount(self):
        return self.__discount

    def get_product_detail(self):
        return self.__detail

    def get_product_thumbnail(self):
        return self.__thumbnail

    def get_product_images(self):
        return self.__images

    def get_product_more_detailed_images(self):
        return self.__more_detailed_images

    def get_product_type(self):
        return self.__type

    def get_reviews(self):
        return self.__reviews

    def set_product_id(self, id):
        self.__id = id

    def set_product_name(self, name):
        self.__name = name

    def set_product_sku(self, sku):
        self.__sku = sku

    def set_product_quantity(self, quantity):
        self.__quantity = quantity

    def set_product_price(self, price):
        self.__price = price

    def set_product_status(self, status):
        self.__status = status

    def set_product_discount(self, discount):
        self.__discount = discount

    def set_product_detail(self, detail):
        self.__detail = detail

    def set_product_thumbnail(self, thumbnail):
        self.__thumbnail = thumbnail

    def set_product_images(self, images):
        self.__images = images

    def set_product_more_detailed_images(self, more_detailed_images):
        self.__more_detailed_images = more_detailed_images

    def set_product_type(self, type):
        self.__type = type

    def set_reviews(self, reviews):
        self.__reviews = reviews

    def add_review(self, user, rating, comment):
        review = {"user": user, "rating": rating, "comment": comment}
        self.__reviews.append(review)

    def __str__(self):
        return f"Name: {self.__name}\nDetail: {self.__detail}\nPrice: {self.__price}\nType: {self.__type}"



class Keyboard(Product):
    def __init__(
        self,
        id,
        name,
        sku,
        quantity,
        price,
        status,
        discount,
        detail,
        thumbnail,
        images,
        more_detailed_images,
        switch,
    ):
        super().__init__(
            id,
            name,
            sku,
            quantity,
            price,
            status,
            discount,
            detail,
            thumbnail,
            images,
            more_detailed_images,
            type="keyboard",
        )
        self.__switch = switch

    def get_switch(self):
        return self.__switch

    def set_switch(self, switch):
        self.__switch = switch


class KeyCaps(Product):
    def __init__(
        self,
        id,
        name,
        sku,
        quantity,
        price,
        status,
        discount,
        detail,
        thumbnail,
        images,
        more_detailed_images,
        type="keycaps",
    ):
        super().__init__(
            id,
            name,
            sku,
            quantity,
            price,
            status,
            discount,
            detail,
            thumbnail,
            images,
            more_detailed_images,
            type,
        )


class Switches(Product):
    def __init__(
        self,
        id,
        name,
        sku,
        quantity,
        price,
        status,
        discount,
        detail,
        thumbnail,
        images,
        more_detailed_images,
        type="switches",
    ):
        super().__init__(
            id,
            name,
            sku,
            quantity,
            price,
            status,
            discount,
            detail,
            thumbnail,
            images,
            more_detailed_images,
            type,
        )


class Accessories(Product):
    def __init__(
        self,
        id,
        name,
        sku,
        quantity,
        price,
        status,
        discount,
        detail,
        thumbnail,
        images,
        more_detailed_images,
        type="accessories",
    ):
        super().__init__(
            id,
            name,
            sku,
            quantity,
            price,
            status,
            discount,
            detail,
            thumbnail,
            images,
            more_detailed_images,
            type,
        )


class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        self.products[product] = self.products.get(product, 0) + quantity

    def show_cart(self):
        for item, number in self.products.items():
            return f"Item: {item}, Quantity: {number}"

    def delete_item(self, product):
        del self.products[product]

    def clear_cart(self):
        self.products.clear()
    def calculate_total(self):
        total = 0
        for product, quantity in self.products.items():
            total += product.get_product_price() * quantity
        return total


# Inside the Particulars class in Classes.py
class Particulars:
    def __init__(self, email, phone, address, postalcode, shipping):
        self.email = email
        self.phone = phone
        self.address = address
        self.postalcode = postalcode
        self.shipping = shipping

    def __str__(self):
        return (
            f"Email: {self.email}\n"
            f"Phone: {self.phone}\n"
            f"Address: {self.address}\n"
            f"Postal Code: {self.postalcode}\n"
            f"Shipping Method: {self.shipping}"
        )





class Order:
    def __init__(self, order_number, cart, particulars):
        self.order_number = order_number
        self.cart = cart
        self.particulars = particulars

    # ... other methods ...

    def get_particulars(self):
        return self.particulars

    def set_particulars(self, particulars):
        self.particulars = particulars

    def get_cart(self):
        return self.cart


    def set_cart(self, cart):
       self.cart = cart
class Review:
    def __init__(self, user, product, rating, comment):
        self.user = user
        self.product = product
        self.rating = rating
        self.comment = comment

    def get_user(self):
        return self._user

    def set_user(self, value):
        self._user = value

    def get_product(self):
        return self._product

    def set_product(self, value):
        self._product = value

    def get_rating(self):
        return self._rating

    def set_rating(self, value):
        self._rating = value

    def get_comment(self):
        return self._comment

    def set_comment(self, value):
        self._comment = value


class Wishlist:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_contents(self):
        return [product.get_name() for product in self.products]
