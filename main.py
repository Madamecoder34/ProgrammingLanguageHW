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
    save_laptops(laptops)

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