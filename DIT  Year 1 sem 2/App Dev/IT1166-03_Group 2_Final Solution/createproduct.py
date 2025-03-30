import shelve
from Classes import *


# Load existing catalog from shelf file if it exists
try:
    with shelve.open("catalog_shelf.db") as shelf:
        catalog = shelf.get("catalog", {})
except FileNotFoundError:
    catalog = {}


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


add_product_to_catalog()
