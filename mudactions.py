'''
Bryan Baraoidan
mudactions.py
An object holding the list of actions that can be taken in a mud
'''

class MudActions:
    def __init__(self):
        self.availableActions = {'look':self.look, 'take':self.take,
                'drop':self.drop, 'go':self.go, 'inventory':self.checkInventory,
                'help':self.commandHelp}

    def performAction(self, command_string, player_character, game_world):
        """
        perform the command given that it is a legal defined by the
        player's action attribute
        """
        #The command is a string of one or two words separated by a
        #space. The first one is the actual command name. The 
        #second is the parameter
        command = command_string.lower().split()
        if command[0] in self.availableActions:
            #When using a dict like a switch, all functions must recieve
            #the same arguments since theres no way of calling it
            #individually with different arguments
            return self.availableActions[command[0]](command, player_character, game_world)
        else:
            return "Sorry I do not know that command"

    def look(self, command, player_character, game_world):
        """
        MudRoom object has a builtin __str__ method which allows it to
        be converted to a string easily, summarizing it's attributes to
        be printed to the screen
        """
        return str(game_world.getRoom(player_character.location))

    def take(self, command, player_character, game_world):
        roomItems = game_world.rooms[player_character.location].contents
        result = ""
        if (len(command) < 2):
            result = "What do you want to  pick up?"
        elif (len(command) > 2):
            result = "You can only pick up one item at a time"
        else:
            #The go command's only parameter is the item you wish to pick up
            item = command[1]
            if item in roomItems:
                player_character.addToInventory(item)
                #Remove the item from the current room
                game_world.rooms[player_character.location].removeItem(item)
                result = "You put the " + item + " in your inventory."
            else:
                result = "There is no such item this room"
        return result

    def drop(self, command, player_character, game_world):
        """
        Once removed from the players inventory it should be placed in
        the contents of the room the player is currently in
        """
        result = ""
        if (len(command) < 2):
            result = "What do you want to drop?"
        elif (len(command) > 2):
            result = "You can only drop one item at a time"
        else:
            item = command[1]
            if item in player_character.inventory:
                #Add the item to the room's list of contents
                game_world.rooms[player_character.location].addItem(item)
                player_character.dropItem(item)
                result = "You dropped the " + item
            else:
                result = "You do not have that item in your inventory"
        return result
    
    def checkInventory(self, command, player_character, game_world):
        """
        Describe what the character is currently holding. Basically a
        proxy method to the method of the same name in PlayerCharacter
        """
        return player_character.checkInventory()

    def go(self, command, player_character, game_world):
        """
        Move the player to another room given the path to exists from
        the player's current location
        """
        result = ""
        #The go command consists of the command itself (go) and a
        #parameter (the direction) separated by a space
        if (len(command) == 2):
            direction = command[1]
            #Each room object in the game_world holds a dict of it's exits
            #and the room it leads to
            roomExits = game_world.rooms[player_character.location].exits
            if direction in roomExits.keys():
                player_character.location = roomExits[direction]
                result = "You walk " + direction + "ward\n"
            else:
                result = "There is no exit in that direction"
        else:
            result = "Which way do I go?"
        return result

    def commandHelp(self, command, player_character, game_world):
        help_message = "List of Actions: "
        for command in self.availableActions.keys():
            help_message += command + " "
        return help_message
