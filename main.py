from laptop import Laptop
from storage import save_laptops, load_laptops

laptops = [] #temp list to hold laptops
def add_laptop():
    brand = input("Brand : ")
    model = input("Model : ")
    country = input("Country of Manifacture : ")
    year = int (input("Year of Manifacture : "))
    driveType = input("HDD Specification : ")
    memoryGB = input("Memory(GB) : ")
    cpuType = input("CPU type : ")
    gpuModel = input("GPU type : ")
    speedMHz = input("Speed (MHz) : ")
    screenSize = input("Screen Size : ")    
    sample = {
       "brand": brand,
        "model": model,
        "country": country,
        "year": year,
        "drive_type": driveType,
        "memory_GB": memoryGB,
        "cpu_type": cpuType,
        "gpu_model": gpuModel,
        "speed_mhz": speedMHz,
        "screen_size": screenSize,
    }
    laptops.append(sample)
    print("Sample laptop (dict) added to temp list. Not saved until you press 1")
    print(f"Current temp list: {laptops}")
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
                add_laptop()
               
            case "4":
                break
            case _:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    menu()