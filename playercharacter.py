'''
Bryan Baraoidan
playercharacter.py
This file defines a character in the game world
'''

class PlayerCharacter:
    def __init__(self):
        self.location = 'sr'
        self.inventory = []

    def addToInventory(self, item):
        self.inventory.append(item)

    def dropItem(self, item):
        item_index = self.inventory.index(item)
        droppedItem = self.inventory[item_index]
        self.inventory.remove(item)

    def checkInventory(self):
        checkResult = ""
        if len(self.inventory) > 0:
            checkResult = "You are currently holding: "
            checkResult += ' '.join(self.inventory)
        else: checkResult = "You have nothing in your inventory"
        return checkResult
