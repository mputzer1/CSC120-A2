
#This creates an object class called computer.
class Computer:

    # The following features the core attributes of the computer.
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    #The following constructor initalizes the different attributes of the object computer.
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    """This method updates the price of the computer with the new price in oo_resale_shop
    when called from oo_resale_shop.py by accessing the computer's price attribute in computer.py. 
    This is called in method refurbish and method update_price.
    """
    def update_price(self, price: int):
        self.price = price

    """This method updates the operating system of the computer when called from 
    oo_resale_shop.py by accessing the computer's operating system attribute in computer.py. 
    This is called in method refurbish.
    """
    def update_os(self, operating_system: str):
        self.operating_system = operating_system
    
    """This method returns information about the computer's attributes when called from 
    oo_resale_shop.py. This is called in method print_inventory.
    """
    def string_computer(self):
        return f"{self.description} {self.processor_type} {str(self.hard_drive_capacity)} {str(self.memory)} {self.operating_system} {str(self.year_made)} {str(self.price)}"
   