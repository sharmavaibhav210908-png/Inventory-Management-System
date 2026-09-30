import pickle
FILE_NAME = "inventory.pkl"

def save_inventory(inventory):
    with open(FILE_NAME, "wb") as f:
        pickle.dump(inventory, f)

def load_inventory():
    try:
        with open(FILE_NAME, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}
    