def addproduct(inventory):
    product_id = input("Enter product ID: ")
    if product_id in inventory:
        print("Product ID already exists. Please use a different ID.")
        return
    name = input("Enter product name: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))

    inventory[product_id] = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    print(f"Product {name} added successfully.")

def viewinventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for product_id, product in inventory.items():
        print(f"ID: {product_id}, Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']:.2f}")


def searchproduct(inventory):
    product_id = input("Enter product ID to search: ")
    if product_id in inventory:
        product = inventory[product_id]
        print(f"Product found: ID: {product_id}, Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']:.2f}")
    else:
        print("Product not found.")

def updateproduct(inventory):
    product_id = input("Enter product ID to update: ")
    if product_id in inventory:
        name = input("Enter new product name: ")
        quantity = int(input("Enter new product quantity: "))
        price = float(input("Enter new product price: "))

        inventory[product_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }
        print(f"Product {name} updated successfully.")
    else:
        print("Product not found.")

def deleteproduct(inventory):
    product_id = input("Enter product ID to delete: ")
    if product_id in inventory:
        del inventory[product_id]
        print(f"Product with ID {product_id} deleted successfully.")
    else:
        print("Product not found.")

def sell_product(inventory):
    product_id = input("Enter product ID to sell: ")
    if product_id in inventory:
        quantity_to_sell = int(input("Enter quantity to sell: "))
        if quantity_to_sell <= inventory[product_id]["quantity"]:
            inventory[product_id]["quantity"] -= quantity_to_sell
            print(f"Sold {quantity_to_sell} units of {inventory[product_id]['name']}.")
            if inventory[product_id]["quantity"] == 0:
                product_name = inventory[product_id]["name"]
                del inventory[product_id]
                print(f"Product {product_name} is now out of stock and removed from inventory.")
        else:
            print("Insufficient stock to complete the sale.")
    else:
        print("Product not found.")

