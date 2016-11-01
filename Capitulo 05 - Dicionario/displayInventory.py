game_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    total_items = 0
    print("Inventory: ")
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_items += v

    print('Total number of items: ' + str(total_items))


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

display_inventory(game_inventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print(dragonLoot)
display_inventory(add_to_inventory(game_inventory, dragonLoot))
