#This program represents two functions. The first function accepts the inventory
#of a Pokemon Trainer as a dictionary in the form {Item:Qty} and displays it
#in the command console. The second function accepts an inventory as described
#above and then adds whatever loot a defeated opponent drops, which is presented
#in the form of a list of strings.



#Display inventory by retrieving key (k) and value (v) for each piece of inventory
#and printing them. Then calculates and prints total pieces in inventory.
def displayInventory(inv):
    print('Inventory')
    totalItems = 0
    for k,v in inv.items():
        print((k.upper() + ': ' + str(v)))
        totalItems = totalItems + v
    print('TOTAL ITEMS: ' + str(totalItems) + '\n')

#This function scans through each piece of inventory in addedLoot. If it is a new piece of inventory
#a new item is added to the dictionary with value zero and then incremented. If it is an existing 
#piece of inventory, the value is just increased by 1.
def addToInventory(inv,addedLoot):
        for loot in addedLoot:
            inv.setdefault(loot,0)
            inv[loot] = inv[loot] + 1

inventory1 = {'Antidote': 3, 'Super Potion': 25, 'Revive': 10, 'Water Stone': 1, 'Poke Ball': 16, 'Master Ball':1}
displayInventory(inventory1)
rocketLoot = ['Poke Ball', 'Antidote', 'Escape Rope', 'Poke Ball']
addToInventory(inventory1,rocketLoot)
displayInventory(inventory1)