# playersStuffs = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# def displayInventory(inventory):
#    print('Inventory :')
#    stuff_total = 0
#    for k, v in inventory.items():
#        print(str(v) + ' ' + k)
#        stuff_total += v
#    print("Total number of items: " + str(stuff_total))
# displayInventory(playersStuffs)
       



#List to Dictionary Function for Fantasy Game Inventory
inv = {'gold coin':42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby',]
def addToInventory(inventory, addedItems):
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        stuff_total += v
    print("Total number of items: " + str(stuff_total))
addToInventory(inv,dragonLoot)
    