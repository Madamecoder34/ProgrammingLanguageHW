import json

def save_laptops(Laptops, filename="laptops.json"):
    with open(filename, "w") as f:
        json.dump([l.to_dict() for l in Laptops], f, indent=4)
    print(f"{len(Laptops)} records have been saved to '{filename}'.")    

def load_laptops(filename="laptops.json"):
    laptops = []
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            # import here to avoid circular imports during module import time
            from laptop import Laptop
            laptops = [Laptop.from_dict(item) for item in data]
    except FileNotFoundError:
        print(f"No existing file found at '{filename}'. Starting with an empty list.")  
    return laptops      