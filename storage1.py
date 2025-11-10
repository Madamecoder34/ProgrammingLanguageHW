import json

def save_laptops(Laptops, filename="laptops.json"):
    with open(filename, "w") as f:
        json.dump([l.to_dict() for l in Laptops], f, indent=4, ensure_ascii=False)
    print(f"{len(Laptops)} records have been saved to '{filename}'.")    

def load_laptops(filename="laptops.json"):
    laptops = []
    try:

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            # import here to avoid circular imports during module import time
            from laptop import Laptop
            laptops = [Laptop.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Warning: '{filename}' is empty or not valid JSON.")
        return []
    return laptops