INVENTORY MANAGEMENT SYSTEM
============================

This is a simple Python Inventory Management System.


PROJECT STRUCTURE
-----------------
InventoryManagement/
│
├── main.py
├── inventory.py
├── storage.py
├── README.txt
└── inventory.pkl       (created automatically after saving)


MODULES
-------

1. main.py
   - Main program
   - Displays the menu
   - Takes the user's choice
   - Calls functions from inventory.py and storage.py

2. inventory.py
   - Contains inventory operations
   - Add product
   - View inventory
   - Search product
   - Update product
   - Delete product
   - Sell product

3. storage.py
   - Handles permanent data storage
   - Uses the pickle module
   - Saves and loads the inventory


DATA STRUCTURE
--------------

The inventory is stored using a LIST of DICTIONARIES.

Example:

inventory = [
    {
        "id": 101,
        "name": "Keyboard",
        "price": 799,
        "quantity": 10
    },
    {
        "id": 102,
        "name": "Mouse",
        "price": 499,
        "quantity": 15
    }
]


PICKLE
------

The pickle module is used to save the complete inventory list
into a file called:

inventory.pkl

When the program starts, the saved data is loaded from the file.

When the user selects Save Inventory or Exit, the current data
is saved using pickle.


HOW TO RUN
----------

1. Keep main.py, inventory.py and storage.py in the same folder.
2. Open the folder in Python IDLE, VS Code, PyCharm, or another Python IDE.
3. Run main.py.
4. Select options from the menu.


MENU
----

1. Add Product
2. View Inventory
3. Search Product
4. Update Product
5. Delete Product
6. Sell Product
7. Save Inventory
8. Exit


IMPORTANT
---------

The purpose is to demonstrate:
- Lists
- Dictionaries
- Functions
- Modules
- Loops
- Conditional statements
- File handling
- Pickle
- Inventory management
