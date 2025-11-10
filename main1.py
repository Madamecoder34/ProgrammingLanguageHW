from laptop import Laptop
from storage import save_laptops, load_laptops
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

  with open("laptops.json", "r", encoding="utf-8") as f:

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

    if not laptops:
        print("\n No laptop found with that has inch.\n")

    if find_inch:
       print("\nFound Laptop(s):")
    for l in find_inch:
           print(find_inch)
    print(laptops.found)
    




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
            case _:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    menu()