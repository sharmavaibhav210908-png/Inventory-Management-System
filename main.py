import inventory
import storage

def main():
    inventory_data = storage.load_inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Sell Product")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.addproduct(inventory_data)
            storage.save_inventory(inventory_data)
        elif choice == "2":
            inventory.viewinventory(inventory_data)
        elif choice == "3":
            inventory.searchproduct(inventory_data)
        elif choice == "4":
            inventory.updateproduct(inventory_data)
            storage.save_inventory(inventory_data)
        elif choice == "5":
            inventory.deleteproduct(inventory_data)
            storage.save_inventory(inventory_data)
        elif choice == "6":
            inventory.sell_product(inventory_data)
            storage.save_inventory(inventory_data)
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()