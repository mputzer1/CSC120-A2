from typing import Dict, Optional
import computer

class ResaleShop:

    # What attributes will it need?

    inventory : Dict[int, Dict]
    itemID: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = {}
        self.itemID = 0

    # What methods will you need?

    def buy(self, computer: object):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID
    
    def update_price(self, item_id: int, new_price: int, computer: object):
        if item_id in self.inventory:
            self.inventory[item_id].update_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
    
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id].string_computer()}')
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.update_price(0) # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.update_price(250) # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.update_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_price(1000) # recent stuff

            if new_os is not None:
                computer.update_os(new_os) # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")