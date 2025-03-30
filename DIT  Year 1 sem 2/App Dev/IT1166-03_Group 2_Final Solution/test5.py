import shelve




with shelve.open("products.db", writeback=True) as db:
    if "Products" in db:
        productDict = db["Products"]
        for id, product in productDict.items():
            if product.get_product_name() == "Keychron V3":
                user = "John"
                rating = 5
                comment = "Great keyboard!"
                product.add_review(user, rating, comment)
                db["Products"] = productDict
                print("Review added successfully.")
            else:
                print("Product not found in catalog.")
                    