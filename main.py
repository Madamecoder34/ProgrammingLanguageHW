from laptop import Laptop
from storage import save_laptops, load_laptops

laptops = load_laptops()

def add_laptop():
    brand = input("Brand: ")
    model = input("Model: ")
    country = input("Country of Manufacture: ")
    year = int(input("Year of Manufacture: "))
    driveType = input("Hard Drive Specification (HDD/SSD): ")
    memoryGB = int(input("Memory Size (GB): "))
    cpuType = input("CPU Type: ")
    gpuModel = input("GPU Model: ")
    speedMHz = int(input("CPU Speed (MHz): "))
    screenSize = float(input("Screen Size (inches): "))
    laptops.append(Laptop(brand, model, country, year, driveType, memoryGB, cpuType, gpuModel, speedMHz, screenSize))
    print("Laptop added successfully.")

def print_laptops():
    for i, l in enumerate(laptops, start=1):
        print(f"{i}. {l.brand} {l.model} ({l.year}) - {l.memoryGB}GB RAM, {l.driveType}") 

def find_laptop():
    brand = input("Enter brand to search: ") 
    model = input("Enter model to search: ")   
    for l in laptops:
        if l.brand == brand and l.model == model:
            print(l.to_dict())
            return
    print("Laptop is not found.")

def same_screen_size():
    size = float(input("Screen Size: "))
    filtered = [l.to_dict() for l in laptops if l.screenSize == size]
    print(filtered if filtered else "Not found.")

def modify_laptop():
    brand = input("Brand: ")
    model = input("Model: ")
    for l in laptops:
        if l.brand == brand and l.model == model:
            field = input("Field to modify: ")
            if hasattr(l, field):
                new_value = input("New value: ")
                # Convert to appropriate type if it's a numeric field
                if field in ["year", "memoryGB", "speedMHz"]:
                    new_value = int(new_value)
                elif field == "screenSize":
                    new_value = float(new_value)
                setattr(l, field, new_value)
                print("Updated.")
                return
            else:
                print("Invalid field.")
                return
    print("Laptop is not found.")

def delete_laptop():
    brand = input("Brand: ")
    model = input("Model: ")
    for i, l in enumerate(laptops):
        if l.brand == brand and l.model == model:
            laptops.pop(i)
            print("Deleted.")
            return
    print("Laptop is not found.")

def menu():
    while True:
        print("""
1. Print to file
2. Read from file
3. Exit
""")
        choice = input("Choice: ")

        match choice:
            case "1":
                save_laptops(laptops)
            case "2":
                loaded = load_laptops()
                for l in loaded:
                    print(l.to_dict())
            case "3":
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()