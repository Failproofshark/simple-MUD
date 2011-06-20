'''
Bryan Baraoidan
mudroom.py
This file contains the definition for a room in the game world
'''

class MudRoom:
    def __init__(self, name, description, contents, exits):
        """
        str: name, description
        str list: contents
        str dict: exits
        """
        self.name = name
        self.description = description
        self.contents = contents
        self.exits = exits

    def __str__(self):
        """String version of Room Object"""
        stringForm = self.name + "\n===========\n" + \
                self.description + "\n\n"
        stringForm += "Items that are currently in the room: "
        if len(self.contents) > 0:
            for item in self.contents:
                stringForm += item + " "
        else:
            stringForm += "None"
        stringForm += "\n\nPaths out of this room: "
        for path in self.exits.keys():
            stringForm += path + " "
        stringForm += "\n"
        return stringForm

    def addItem(self, item):
        """
        Add an item to the room, whether it be a character entering it
        or an item left behind 
        """
        self.contents.append(item)

    def removeItem(self, item):
        """
        When a character picks up (takes) an item remove it from the
        room
        """
        if item in self.contents:
            self.contents.remove(item)
