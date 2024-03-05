#imports useful containers from the typing module
from typing import Dict, Optional

#imports the computer object
import computer

#creates an object called ResaleShop
class ResaleShop:

    #The following are the core attributes of the resale shop
    inventory : list
    itemID: int

    """
    The following constructor initalizes the attributes of the resale shop. 
    The inventory begins with nothing in it while the itemID starts at 0.
    """
    def __init__(self):
        self.inventory = {}
        self.itemID = 0

    
    """
    Takes in a Dict containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    """
    def buy(self, computer: object):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID
    
    """
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """
    def update_price(self, item_id: int, new_price: int, computer: object):
        if item_id in self.inventory:
            self.inventory[item_id].update_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
    
    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id].string_computer()}')
        else:
            print("No inventory to display.")

    """
    Updates the price of computer based on the year made 
    and updates the operating system.
    """
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