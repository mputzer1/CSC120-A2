#from oo_resale_shop import item_id ---) Not working


class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
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

    def update_price(self, price: int):
        self.price = price

    def update_os(self, operating_system: str):
        self.operating_system = operating_system
    
    def string_computer(self):
        return f"{self.description} {self.processor_type} {str(self.hard_drive_capacity)} {str(self.memory)} {self.operating_system} {str(self.year_made)} {str(self.price)}"
   

    # What methods will you need?