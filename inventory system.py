# Simple inventory system using lists
inventory = []  # List to store items
quantities = []  # List to store corresponding quantities

def add_item():
    # Function to add or update an item in the inventory
    item = input("Enter item name: ").strip().lower()
    quantity = int(input("Enter quantity: "))

    if item in inventory:
        index = inventory.index(item)  # Find the index of the item
        quantities[index] += quantity  # Update quantity
    else:
        inventory.append(item)  # Add new item
        quantities.append(quantity)  # Add new quantity

    print(str(quantity) + " " + item + "(s) added to inventory.")

def retrieve_item():
    # Function to retrieve an item from the inventory
    item = input("Enter item name to check: ").strip().lower()

    if item in inventory:
        index = inventory.index(item)
        print(item.capitalize() + " quantity: " + str(quantities[index]))
    else:
        print(item.capitalize() + " is not in the inventory.")

def total_inventory():
    # Function to display all items with their quantities and total quantity count
    print("\nTotal Inventory:")
    total = 0

    if not inventory:
        print("Inventory is empty.")
    else:
        for i in range(len(inventory)):
            print(inventory[i].capitalize() + ": " + str(quantities[i]))
            total += quantities[i]

        print("Total quantity of all items in inventory: " + str(total))

def main():
    # Main function to display menu and handle user choices
    while True:
        print("\nInventory System Menu:")
        print("1. Add/Update Item")
        print("2. Retrieve Item")
        print("3. Show Total Inventory")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            retrieve_item()
        elif choice == "3":
            total_inventory()
        elif choice == "4":
            print("Exiting inventory system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the inventory system
main()
