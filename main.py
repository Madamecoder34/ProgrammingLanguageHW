from laptop import Laptop
from storage import save_laptops, load_laptops

laptops = [] #temp list to hold laptops
##def add_laptop():
    ## yasemin bura senin laptops a ekleme
def save_and_clear():
    existing = load_laptops()
    normalized = []
    for item in laptops:
        if isinstance(item, Laptop):
            normalized.append(item)
        elif isinstance(item, dict):
            # dict ise Laptop.from_dict kullan
            normalized.append(Laptop.from_dict(item))
        else:
            # desteklenmeyen tipleri atla ve uyar
            print(f"Warning: skipping unsupported item in temp: {item!r}")
    merged = existing + normalized
    save_laptops(merged)
    laptops.clear()
    print("Temporary list cleared after saving.")

def read_laptops():
    loaded = load_laptops()
    if not loaded:
        print("No laptops found.")
    for i, l in enumerate(loaded, start=1):
        print(f"Laptop {i}: {l.to_dict()}")

def menu():
    while True:
        print("""
1. Print to file
2. Read from file
3. (For testing) Add a sample laptop to temp list
4. Exit
""")
        choice = input("Choice: ")

        match choice:
            case "1":
                save_and_clear()
            case "2":
                read_laptops()
            case "3":
                # sadece test amaçlı, gerçek eklemeyi ark. yapacak
                sample = Laptop("Dell","XPS","USA",2022,"SSD",16,"i7","RTX3050",3200,15.6)
                laptops.append(sample)
                print("Sample laptop added to temp list. (Not saved until you press 1)")
            case "4":
                break
            case _:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    menu()