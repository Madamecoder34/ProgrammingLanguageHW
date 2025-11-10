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
3. Add a laptop
4. Exit
5.
""")
        choice = input("Choice: ")

        match choice:
            case "1":
                save_and_clear()
            case "2":
                read_laptops()
            case "3":
                # sadece test amaçlı: dict şeklinde bir sample ekle (sonra 1 ile kaydedilir)
                brand = input("brand = ")
                model = input("model = ")
                sample = {
                    "brand": brand,
                    "model": model,
                    "country": None,
                    "year": None,
                    "drive_type": None,
                    "memory_GB": None,
                    "cpu_type": None,
                    "gpu_model": None,
                    "speed_mhz": None,
                    "screen_size": None,
                }
                laptops.append(sample)
                print("Sample laptop (dict) added to temp list. Not saved until you press 1")
                print(f"Current temp list: {laptops}")
            case "4":
                break
            case _:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    menu()