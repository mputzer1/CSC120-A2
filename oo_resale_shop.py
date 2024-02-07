from typing import Dict, Optional

class ResaleShop:

    # What attributes will it need?

    item_id: int
    computer: dict
    inventory: dict

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(item_id: int, inventory: dict, computer: dict):
        this.inventory = inventory
        this.item_id = item_id
        this.computer = computer

    # What methods will you need?
    
    inventory : Dict[int, Dict] = {}
    itemID = 0

    def buy(computer: Dict):
        global itemID
        itemID += 1 # increment itemID
        this.inventory[itemID] = computer
        return itemID
    
    def sell(item_id: int):
        if this.item_id in inventory:
            del inventory[this.item_id]
            print("Item", this.item_id, "sold!")
        else: 
            print("Item", this.item_id, "not found. Please select another item to sell.")

    def print_inventory(inventory: dict):
    # If the inventory is not empty
        if this.inventory:
            # For each item
            for this.item_id in this.inventory:
                # Print its details
                print(f'Item ID: {this.item_id} : {this.inventory[this.item_id]}')
        else:
            print("No inventory to display.")

    def main():
        buy({"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"High Sierra", "year_made":2019, "price":1000})
        print_inventory()

    main()