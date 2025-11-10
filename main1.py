from laptop import Laptop
from storage1 import save_laptops, load_laptops
import json
import os

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
    screenSize = float(input("Screen Size : "))    
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
    
def find_laptop():
    json_path = os.path.join(os.path.dirname(__file__), "laptops.json")
    with open(json_path, "r", encoding="utf-8") as f:
        laptops = json.load(f)
    brand = input("Enter brand to search: ").strip()
    model = input("Enter model to search: ").strip()

    found = [l for l in laptops if l ["brand"].lower() == brand.lower() and l["model"].lower() == model.lower()]
    if found:
        print("\nFound Laptop(s):")
        for l in found:
            print(found)
    else:
        print("\n No laptop found with that brand and model.\n")

def print_all():
    json_path = os.path.join(os.path.dirname(__file__), "laptops.json")

    # Read the JSON file
    with open(json_path, "r", encoding="utf-8") as f:
        laptops = json.load(f)

    if not laptops:
        print("\nNo laptops in the list.\n")
        return

    print("\nAll laptops in the list:\n")
    for l in laptops:
        print(l)
    print()
    
def show_laptops_according_to_size():
    json_path = os.path.join(os.path.dirname(__file__), "laptops.json")
    with open(json_path, "r", encoding="utf-8") as f:
        laptops = json.load(f)

    inch = float(input("Enter inch value for see the laptos : ")) 

    find_inch = [l for l in laptops if l ["screen_size"] == inch ]

    if not find_inch:  
        print(f"\nNo laptop found with {inch} inch screen size.\n")
    else:
        print(f"\nFound {len(find_inch)} laptop(s) with {inch} inch screen size:")
        for laptop in find_inch:  
            print(f"Brand: {laptop['brand']}, Model: {laptop['model']}, Screen: {laptop['screen_size']}\"")

def modify_laptop():
    """7. Modify laptop record"""
    print("\n--- Modify Laptop ---")
    
    # Mevcut laptopları yükle
    laptops_list = load_laptops()
    
    if not laptops_list:
        print("No laptops found in database!")
        return
    
    brand = input("Enter brand: ").strip()
    model = input("Enter model: ").strip()
    
    # Laptop'u bul
    found_index = -1
    for i, laptop in enumerate(laptops_list):
        if laptop.brand.lower() == brand.lower() and laptop.model.lower() == model.lower():
            found_index = i
            break
    
    if found_index == -1:
        print("Laptop not found!")
        return
    
    print(f"\nFound: {laptops_list[found_index].brand} {laptops_list[found_index].model}")
    
    # TÜM alanları göster ve seçenek sun
    print("\nWhich field do you want to modify?")
    print("1. Brand")
    print("2. Model") 
    print("3. Country")
    print("4. Year")
    print("5. Drive Type")
    print("6. Memory (GB)")
    print("7. CPU Type")
    print("8. GPU Model")
    print("9. Speed (MHz)")
    print("10. Screen Size")
    
    choice = input("Enter your choice (1-10): ").strip()
    new_value = input("Enter new value: ").strip()
    
    # Seçime göre güncelle
    if choice == "1":
        laptops_list[found_index].brand = new_value
    elif choice == "2":
        laptops_list[found_index].model = new_value
    elif choice == "3":
        laptops_list[found_index].country = new_value
    elif choice == "4":
        laptops_list[found_index].year = int(new_value)
    elif choice == "5":
        laptops_list[found_index].driveType = new_value
    elif choice == "6":
        laptops_list[found_index].memoryGB = new_value
    elif choice == "7":
        laptops_list[found_index].cpuType = new_value
    elif choice == "8":
        laptops_list[found_index].gpuModel = new_value
    elif choice == "9":
        laptops_list[found_index].speedMHz = new_value
    elif choice == "10":
        laptops_list[found_index].screenSize = float(new_value)
    else:
        print("Invalid choice!")
        return
    
    # Değişiklikleri kaydet
    save_laptops(laptops_list)
    print("Laptop updated successfully!")

def delete_laptop():
    """8. Delete laptop record"""
    print("\n=== DELETE LAPTOP ===")
    laptops_list = load_laptops()
    
    if not laptops_list:
        print("No laptops found in database!")
        return
    
    brand = input("Enter brand to delete: ")
    model = input("Enter model to delete: ")
    
    new_list = []
    deleted = 0
    
    for laptop in laptops_list:
        if laptop.brand.lower() == brand.lower() and laptop.model.lower() == model.lower():
            deleted += 1
        else:
            new_list.append(laptop)
    
    if deleted > 0:
        save_laptops(new_list)
        print(f"Deleted {deleted} laptop(s) successfully!")
    else:
        print("Laptop not found!")

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
4. Find a laptop 
5. Print all laptops
6. Find laptops according to screen size 
7. Modify laptop record
8. Delete laptop record
9. Exit program
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
                find_laptop()
            case "5":
                print_all()
            case "6":
                show_laptops_according_to_size()
            case "7":
                modify_laptop()
            case "8":
                delete_laptop()
            case "9":
                print("Program closed. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    menu()