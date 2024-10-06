#here is where we create our classes and methods them import them to be used in main file to build program

class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None #none is a value in python. we can use set method to give it a value later
        self.linked_rooms = {} #empty dictionary = allows you to add to it as you go along. dictionary is a list in key value pairs
        self.character = None#need to do setters and getters
        self.item = None
        

    def get_description(self):
        return self.description #no input for user, but value available for methods to use

    def set_description(self, room_description):
        self.description = room_description #setting method, varibale gets a value we input via class method

    def describe(self):
        print(self.description)

    def set_name(self, room_name):#name value we give in brackets when using method replaces self
        self.name = room_name

    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item

    def link_room(self, room_to_link, direction):#method to link rooms
        self.linked_rooms[direction] = room_to_link #[] to access key value pairs in our dictionary

    def get_details(self):
        print(f"You are in the {self.name}.")
        print("-------------------------------------------------------")#to give video game feel in terminal
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}.")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You cannot go that way.")
            return self #stay where you are


class Locked_room(Room):
    def __init__(self, room_name):
        super().__init__(room_name)
        

    def open_door(self):
        inventory = []
        if "key" in inventory:
            print("You used the key to open the door! The Mystic Mansion has been escaped.")
            return False
        else:
            print("The door is locked.")
            return True











