"""
Name: Tan Hng Wu
Student Admin no: 231691N
Tutorial Group: Group 3
"""
from stationary import Stationary as Stationary
import re
from restockdetail import RestockDetail
from queue import Queue


stationary_Inventory = []
RestockingQ = Queue()
records_per_row = 1


def add_stationary():
    id_Pattern = r"^PD[\d]{4}$"  # Alphanumeric characters, allowed
    name_Pattern = r"^[\w\s]+$"  # Only alphabets and spaces allowed
    category_Pattern = r"^[\w\s]+$"  # Only alphabets and spaces allowed
    brand_Pattern = r"^[\w\s]+$"  # Only alphabets and spaces allowed
    year_Pattern = r"^\d{4}$"  # Four digits representing a year

    # Input validation loop
    while True:
        checkIdExists = True
        prod_id = input("Enter Product ID: ")
        for product in stationary_Inventory:
            if prod_id == product.prod_id:
                print("Product ID is already in the inventory")
                return
        if re.match(id_Pattern, prod_id) and checkIdExists:
            break
        else:
            print(
                "Invalid Product ID format. Please use a unique alphanumeric characters"
                " in the format PD(4 Digit Number)."
            )
            return

    while True:
        prod_name = input("Enter Product Name: ")
        if re.match(name_Pattern, prod_name):
            break
        else:
            print("Invalid Product Name format. Please use only alphabets and spaces.")
            return

    while True:
        category = input("Enter Product Category: ")
        if re.match(category_Pattern, category):
            break
        else:
            print("Invalid Category format. Please use only alphabets and spaces.")
            return

    while True:
        brand = input("Enter Brand: ")
        if re.match(brand_Pattern, brand):
            break
        else:
            print("Invalid Brand format. Please use only alphabets and spaces.")
            return

    while True:
        supplier_since = input(
            "Please enter the year this supplier started supplying this product: "
        )
        if re.match(year_Pattern, supplier_since):
            # Convert supplier_since to integer after validation
            supplier_since = int(supplier_since)
            break
        else:
            print("Invalid Year format. Please enter a valid four-digit year.")
            return

    # Create new stationary object and add it to inventory
    new_Stationary = Stationary(prod_id, prod_name, category, brand, supplier_since, 0)
    stationary_Inventory.append(new_Stationary)
    print("Product added successfully!")


def display_stationary():
    if not stationary_Inventory:
        print("There are currently no products in the system!")
    else:
        print(f"-" * 30)
        print("Products List:")
        for product in stationary_Inventory:
            print(
                f"Product ID: {product.prod_id}\nProduct Name: {product.prod_name}\nProduct Category: "
                f"{product.category}"
                f"\nBrand: {product.brand}\nSupplier Year: {product.supplier_since}\n"
                f"Stock: {product.stock}",
                end="\n",
            )
            print(f"-" * 30)


def bubble_sort_stationary():
    n = len(stationary_Inventory)
    passNo = 1
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Bubble the largest item to the end
        for j in range(i):
            if stationary_Inventory[j].category < stationary_Inventory[j + 1].category:
                # Swap the j and j+1 items
                tmp = stationary_Inventory[j]
                stationary_Inventory[j] = stationary_Inventory[j + 1]
                stationary_Inventory[j + 1] = tmp
        print(f"Pass: {passNo}")
        print(f"----------------------------------------------------")
        for product in stationary_Inventory:
            print(f"prod_id: {product.prod_id}")
        print(f"----------------------------------------------------")

        passNo += 1
    print("\n\n")
    display_stationary_recursive()


def insertion_sort_stationary():
    n = len(stationary_Inventory)
    passNo = 1

    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = stationary_Inventory[i]
        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        while pos > 0 and value.brand < stationary_Inventory[pos - 1].brand:
            # Shift the items to the right during the search
            stationary_Inventory[pos] = stationary_Inventory[pos - 1]
            pos -= 1
        # Put the saved value into the open slot.
        stationary_Inventory[pos] = value
        print(f"Pass: {passNo}")
        print(f"----------------------------------------------------")
        for product in stationary_Inventory:
            print(f"prod_id: {product.prod_id}")
        print(f"----------------------------------------------------")
        passNo += 1
    print("\n\n")
    display_stationary_recursive()


def selection_sort():
    n = len(stationary_Inventory)
    passNo = 1

    for i in range(n - 1):
        # Assume the ith element is the largest.
        smallNdx = i
        # Determine if any other element contains a largest value.
        for j in range(i + 1, n):
            if stationary_Inventory[j].prod_id > stationary_Inventory[smallNdx].prod_id:
                smallNdx = j
        # Swap the ith value and smallNdx value only if the largest
        # value is not already in its proper position.
        if smallNdx != i:
            tmp = stationary_Inventory[i]
            stationary_Inventory[i] = stationary_Inventory[smallNdx]
            stationary_Inventory[smallNdx] = tmp

        print(f"Pass: {passNo}")
        print(f"----------------------------------------------------")
        for product in stationary_Inventory:
            print(f"prod_id: {product.prod_id}")
        print(f"----------------------------------------------------")
        passNo += 1

    print("\n\n")
    display_stationary_recursive()


def merge_sort(stationary_Inventory):
    if len(stationary_Inventory) <= 1:
        return stationary_Inventory
    else:
        # Compute the midpoint
        mid = len(stationary_Inventory) // 2
        # Split the list and perform the recursive step
        leftHalf = merge_sort(stationary_Inventory[:mid])
        rightHalf = merge_sort(stationary_Inventory[mid:])
        # Merge the two sorted sublists
        newList = mergeSortedLists(leftHalf, rightHalf)

        return newList


def mergeSortedLists(listA, listB):
    # Create the new list and initialise the list markers
    newList = list()
    a = 0
    b = 0
    # Merge the two lists together until one is empty
    while a < len(listA) and b < len(listB):
        if listA[a].category < listB[b].category:
            newList.append(listA[a])
            a += 1
        elif listB[b].category == listA[a].category:
            if listA[a].stock < listB[b].stock:
                newList.append(listA[a])
                a += 1
            else:
                newList.append(listB[b])
                b += 1
        else:
            newList.append(listB[b])
            b += 1
    # If listA contains more items, append remaining items to
    # newList
    while a < len(listA):
        newList.append(listA[a])
        a += 1
    # If listB contains more items, append remaining items to
    # newList
    while b < len(listB):
        newList.append(listB[b])
        b += 1
    print(f"New List: ")
    print(f"----------------------------------------------------")
    for product in newList:
        print(f"prod_id: {product.prod_id}")
    print(f"----------------------------------------------------")

    return newList


def enqueue_restock_detail(prod_id, quantity):
    # Check if the product ID exists in the system
    # If product exists, create a RestockDetail object and add it to the queue
    restock_detail = RestockDetail(prod_id, quantity)
    RestockingQ.enqueue(restock_detail)
    print("Restocking arrival queued successfully!\n")
    # print(f"Restock detail for Product ID {prod_id} added to the queue.")


def SortedSequentialSearch(theValues, target):
    n = len(theValues)

    # theValues.sort()
    for i in range(n):
        if theValues[i].prod_id == target:
            return True

    return False


def dequeue_restock_detail():
    print("\n")
    print("Display Pending stock arrival:")
    print("-" * 15)
    item = RestockingQ.dequeue()
    for product in stationary_Inventory:
        if product.prod_id == item.prod_id:
            print(
                f"Product ID: {product.prod_id}\nProduct Name: {product.prod_name}\nProduct Category: "
                f"{product.category}"
                f"\nBrand: {product.brand}\nSupplier Year: {product.supplier_since}\n"
                f"Stock remaining: {product.stock}",
                end="\n",
            )
    print("-" * 15)
    print(f"New Stock: {item.quantity}")
    print("-" * 15 + "\n")
    print(f"Remaining restock in queue: {RestockingQ.__len__()}\n")

    proceed = input("Proceed with restock in queue (Y/N): ")
    if proceed.lower() == "y":
        for product in stationary_Inventory:
            if product.prod_id == item.prod_id:
                product.stock += int(item.quantity)
                print(f"Prod_id: {item.prod_id} updated stock: {product.stock}\n")
    else:
        RestockingQ.enqueue(item)
        print(f"Product {item.prod_id} re-queued!\n")


records_per_row = 1


def display_stationary_recursive():
    if not stationary_Inventory:
        print("There are currently no products in the system!")
    else:
        while True:
            try:
                if records_per_row > 0:
                    break
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        print(f"-" * 30)
        print("Products List:")
        display_records_recursive(stationary_Inventory, 0, records_per_row)
        print(f"-" * 50 * records_per_row)


def display_records_recursive(records, index, records_per_row):
    if index >= len(records):
        return

    attributes = [
        ("Prod id", "prod_id"),
        ("Prod Name", "prod_name"),
        ("Category", "category"),
        ("Brand", "brand"),
        ("Supplier Since", "supplier_since"),
        ("Stocks", "stock"),
    ]

    col_width = 30  # Set a fixed column width for values
    name_width = 15  # Set a fixed column width for attribute names

    for attr_name, attr in attributes:
        for i in range(records_per_row):
            if index + i < len(records):
                product = records[index + i]
                print(
                    f"{attr_name:<{name_width}}: {getattr(product, attr):<{col_width}}",
                    end="",
                )
        print()
    print("\n")
    display_records_recursive(records, index + records_per_row, records_per_row)


def populateData():
    prodList = []
    newStudA = Stationary(
        "PD1020", "Pastel Art Paper", "Paper", "Faber-Castell", 2021, 2000
    )
    prodList.append(newStudA)
    newStudA = Stationary(
        "PD1025", "Mars Lumograph Drawing Pencils", "Pencils", "Staedtler", 2022, 320
    )
    prodList.append(newStudA)
    newStudA = Stationary(
        "PD1015", "Water color Pencils", "Pencils", "Faber-Castell", 2011, 150
    )
    prodList.append(newStudA)
    newStudA = Stationary(
        "PD1050", "Noris 320 fiber tip pen", "Pens", "Staedtler", 2021, 350
    )
    prodList.append(newStudA)
    newStudA = Stationary(
        "PD1001", "Copier Paper (A4) 70GSM", "Paper", "PaperOne", 2021, 1500
    )
    prodList.append(newStudA)
    newStudA = Stationary(
        "PD1033", "Scientific Calculator FX-97SG X", "Calculator", "Casio", 2022, 50
    )
    prodList.append(newStudA)
    newStudA = Stationary(
        "PD1005",
        "POP Bazic File Separator Clear",
        "Office Supplies",
        "Popular",
        2000,
        500,
    )
    prodList.append(newStudA)

    print("Data populated!\n")
    return prodList


def restocking_menu():
    while True:
        print("Restocking Menu:")
        print("1. Enter new stock arrival")
        print("2. View Number of stock arrival")
        print("3. Service next restock in queue.")
        print("0. Return to Main Menu")
        choice = input("Please select one:")
        if choice == "1":
            while True:
                prod_id = input("Enter Product ID: ")
                if SortedSequentialSearch(stationary_Inventory, prod_id):
                    quantity = input("Enter Quantity: ")
                    enqueue_restock_detail(prod_id, quantity)
                    break
                else:
                    print("Invalid product id. Please try again!")

        elif choice == "2":
            print(f"\nNumber of restocking in queue: {RestockingQ.__len__()}\n")
            #print(RestockingQ.__str__())
        elif choice == "3":
            dequeue_restock_detail()

        elif choice == "0":
            print("Exiting restocking menu...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


def main_menu():
    global stationary_Inventory
    global records_per_row
    while True:
        print("Stationary Management System ")
        print("1. Add a new Stationary.")
        print("2. Display all Stationary.")
        print("3. Sort Stationary via Bubble Sort on Category.")
        print("4. Sort Stationary via Insertion Sort on Brand ")
        print("5. Sort Stationary via Selection Sort on Prod id ")
        print(
            "6. Sort Stationary via Merge Sort on Category followed by stock in ascending order "
        )
        print("7. Go to Restocking Menu ")
        print("8. Set number of records per row to display")
        print("9. Populate data")
        print("0. Exit program")
        choice = input("Please select one:")

        if choice == "1":
            add_stationary()
        elif choice == "2":
            display_stationary_recursive()
        elif choice == "3":
            if not stationary_Inventory:
                print("There are currently no products in the Inventory!")
            else:
                bubble_sort_stationary()
        elif choice == "4":
            if not stationary_Inventory:
                print("There are currently no products in the Inventory!")
            else:
                insertion_sort_stationary()
        elif choice == "5":
            selection_sort()
        elif choice == "6":
            tempList = merge_sort(stationary_Inventory)
            print("\n\n")
            stationary_Inventory.clear()
            stationary_Inventory = tempList
            display_stationary_recursive()
        elif choice == "7":
            restocking_menu()
        elif choice == "8":
            records_per_row = int(
                input("Enter the number of records to display per row: ")
            )
        elif choice == "9":
            stationary_Inventory = populateData()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main_menu()
