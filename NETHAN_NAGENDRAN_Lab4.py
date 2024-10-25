class Computer:
    def __init__(self, serial_number, manufacturer, model, processor, ram, display_size):
        self.serial_number = serial_number
        self.manufacturer = manufacturer
        self.model = model
        self.processor = processor
        self.ram = ram
        self.display_size = display_size

    def print_info(self):
        print(f"Serial Number: {self.serial_number}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Processor: {self.processor}")
        print(f"RAM: {self.ram}")
        print(f"Display: {self.display_size}")



class Laptop(Computer):
    def __init__(self, serial_number, manufacturer, model, processor, ram, display_size, weight, is_touch_screen):
        super().__init__(serial_number, manufacturer, model, processor, ram, display_size)
        self.weight = weight
        self.is_touch_screen = is_touch_screen

    def print_info(self):
        super().print_info()
        print(f"Weight: {self.weight}")
        print(f"Touch Screen: {self.is_touch_screen}")



class Desktop(Computer):
    def __init__(self, serial_number, manufacturer, model, processor, ram, display_size, desktop_type):
        super().__init__(serial_number, manufacturer, model, processor, ram, display_size)
        self.desktop_type = desktop_type

    def print_info(self):
        super().print_info()
        print(f"Type: {self.desktop_type}")


#outputs
laptop = Laptop("A001", "Apple", "MacBook Air", "Apple M1", "16GB", "13.3\" "" ", "2.7 lbs", False)
print("Laptop Info:")
laptop.print_info()

print('\n')

desktop = Desktop("A002", "Dell", "Inspiron", "core i7", "32GB", "27\" ", "All-in-One")
print("Desktop Info:")
desktop.print_info()
