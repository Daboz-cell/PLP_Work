# Assignment 1: Design Your Own Class (Smartphone Example)

# Parent class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
    
    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")
    
    def charge(self):
        self.battery = 100
        print(f"{self.brand} {self.model} is now fully charged!")

# Child class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        # Inherit attributes from Smartphone
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system
    
    # Polymorphism: redefining the charge method
    def charge(self):
        self.battery = 100
        print(f"{self.brand} {self.model} (Gaming Edition) charges with fast charging ⚡")

# --- Testing ---
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "S23", "256GB", 80)
    phone2 = GamingPhone("Asus", "ROG Phone 7", "512GB", 45, "Liquid Cooling")

    phone1.make_call("0712345678")
    phone2.make_call("0798765432")

    phone1.charge()
    phone2.charge()
