
import shelve


productDict = {}
db = shelve.open("products.db", "c")
try:
    if "Products" in db:
        productDict = db["Products"]
    else:
        db["Products"] = productDict
except IOError:
    print("Error in opening products.db.")

for key, value in productDict.items():
    print(key, value)
    methods = [method for method in dir(value) if callable(getattr(value, method))]
    print("Methods in MyClass:")
    for method in methods:
        print(method)