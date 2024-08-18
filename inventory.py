inventory={}

def add_products(name , quantity):
    if name in inventory:
        inventory[name] =+ quantity
    else:
         inventory[name] = quantity

def remove_product(name, quantity):
    if name in inventory:
        if inventory[name] >= quantity:
            inventory[name] -= quantity
            if inventory[name] == 0:
                del inventory[name]
        else:
            print(f"Not enough stock to remove {quantity} units of {name}.")
    else:
        print(f"{name} does not exist in the inventory.")

def display_inventory():
    if inventory:
        print("Inventory")
        for name, quantity in inventory.items():
            print(f"{name}: {quantity} units")
    else:
        print("Inventory is empty.")

add_products("apple mob" , 30)

add_products("samsung mob" , 80)
add_products("vivo mob" , 90)


remove_product("apple mob" , 10)

display_inventory()





