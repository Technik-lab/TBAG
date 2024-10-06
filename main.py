#import method from class which is in room.py file, so from room is the room file, import Room is the class and its methods

from room import Room
from room import Locked_room
from character import Enemy
from character import Friend
from item import Item

inventory = [] #initial inventory method, tried using item class instead

def take_item(current_item, inventory):
    # Add the current item to the inventory
    inventory.append(current_item.get_name())
    print(f"You have picked up {current_item.get_name()}")



kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
cellar = Room("Cellar")
basement = Room("Basement")
secret_room = Locked_room("Secret Room")
secret_room.open_door()


dave = Enemy("Dave", "A stinky zombie.") #creating enemy, option to talk, weakness for fighting & setting in a location
dave.set_conversation("Braaaaiiinsssss") 
dave.set_weakness("cheese")
dining_hall.set_character(dave)

goblin = Enemy("Goblin", "A small green goblin. It smiles eerily, but it should be easy enough to take on.")
goblin.set_conversation("huh? who're you? you will not make it past me...kehkehkeeehh")
goblin.set_weakness("fire")
cellar.set_character(goblin)

mariette = Friend("mariette", "A gracious elf, who seems kind.", "key")
mariette.set_conversation("Hello traveller. You seem wary from adventure. Your freedom lies in this room.")
mariette.set_gift("gold")
secret_room.set_character(mariette)

cheese = Item()#creating item object. item methods will apply to cheese
cheese.set_name("cheese")
cheese.set_description("Great for sandwiches, weirdly even better for killing zombies.")
kitchen.set_item(cheese)#setting cheese using a room method. methods from different classes only effect their own instances even if methods are named the same

fire = Item()
fire.set_name("fire")
fire.set_description("An etherel fire.It doesn't burn, but the light is bright.")
basement.set_item(fire)

key = Item()
key.set_name("key")
key.set_description("A unique, shiny crystalline key. What a key like this opens you are yet to tell.")
secret_room.set_item(key)

#have to set before we get or will have no value or no updated values is one has been set
kitchen.set_description("A dirty room buzzing with flies. The stench of mold and rotting flesh fill the room.")
ballroom.set_description("A vast room with a shiny wooden floor. Stylish but empty.")
dining_hall.set_description("A large room with ornate decorations, and giant potraits.")
cellar.set_description("A damp, decripit room, full of cobwebs. There are a small pile of bones in the corner.")
basement.set_description("This underground room is full of useless junk. At least that is what you presume.")
secret_room.set_description("In this place you feel the energy of what you can only call magic. You can tell this room contains many secrets.")

kitchen.link_room(dining_hall, "south")
kitchen.link_room(cellar, "east")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(basement, "east")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(secret_room, "south")
secret_room.link_room(ballroom, "north")
cellar.link_room(kitchen, "west")
cellar.link_room(basement, "south")
basement.link_room(cellar, "north")
basement.link_room(dining_hall, "west")


#print(kitchen.get_description())
#dining_hall.get_details()

# title screen in ASCII art, r = red

def title_screen():
    print(r"""
        __    __   _______  __       __   _______    ______   __    __   _______  __       
       |  |  |  | |   ____||  |     |  | |   ____|  /  __  \ |  |  |  | |   ____||  |      
       |  |__|  | |  |__   |  |     |  | |  |__    |  |  |  ||  |__|  | |  |__   |  |      
       |   __   | |   __|  |  |     |  | |   __|   |  |  |  ||   __   | |   __|  |  |      
       |  |  |  | |  |____ |  `----.|  | |  |____  |  `--'  ||  |  |  | |  |____ |  `----. 
       |__|  |__| |_______||_______||__| |_______|  \______/ |__|  |__| |_______||_______| 
                                                                                           
                  __  ___  __    __   _______ .___  ___.  _______ .__   __. 
                 |  |/  / |  |  |  | |   ____||   \/   | |   ____||  \ |  | 
                 |  '  /  |  |  |  | |  |__   |  \  /  | |  |__   |   \|  | 
                 |    <   |  |  |  | |   __|  |  |\/|  | |   __|  |  . `  | 
                 |  .  \  |  `--'  | |  |____ |  |  |  | |  |____ |  |\   | 
                 |__|\__\  \______/  |_______||__|  |__| |_______||__| \__| 
                                                                            
                                                                      
               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     Welcome to the Magical World of Mystic Mansion!
                       Press Enter to start your journey...

    """)

# Example usage: call this function at the start of the game
title_screen()
input()  # Wait for the player to press enter

print("Commands list:\nDirections: north south east west\nFight: fight\nTalk: talk\nInventory: inventory\nHelp: help\nQuit:quit")
print(r"press Enter to continue....")
input()
#main execution loop

print("You open your eyes, with no recollection of how you got to this mysterious place you find yourself. You have no time to ponder your confusion, the feeling this is not a place to stay overwhelms you.")

current_room = kitchen

while True:#running indefinately, we can exit with other commands like break or falsse
    print("\n")
    current_room.get_details()#details of room currently in
    inhabitant = current_room.get_character()#setting character in a room as an inhabitant
    print("-------------------------------------------------------")
    if inhabitant is not None:
        inhabitant.describe()
    an_item = current_room.get_item()#setting item in room as an item
    if an_item is not None:
        an_item.describe_item()
        pick_up = input("Do you wish to pick up the item? (yes/no): ")

        if pick_up.lower() == "yes":
            take_item(an_item, inventory) #put item in an inventory
            current_room.set_item(None) #item no longer in the room once picked up

        elif pick_up.lower() == "no":
            print(f"You chose not to pick up {an_item}")

    command = input("> ")#code waits for input of user

    if command.lower() in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)#depending on input new room then loops back

    elif command.lower() == "quit":
        print("\n")
        print("You flee from responsibility.")
        break

    elif command.lower() == "inventory":
        print("\n")
        if len(inventory) == 0:
            print("Your inventory is empty.")
        else:
            print("You are carrying:")
            for item in inventory:
                print(f"- {item}")
                if item == "key":
                    print("You have the crystal key. You are able to open a portal and escape the mystic mansion.")
                    break#breaks out of the for loop. unnecessary?
            else:
                continue#executes if for loop doesn't break/u don't have key
            break#breaks the overall while true loop
    
    elif command.lower() == "talk":
        print("\n")
        inhabitant.talk()       
         
    elif command.lower() == "fight":
        print("\n")
        print("What will you fight with?")
        fight_with = input("Enter item here: ")
        result = inhabitant.fight(fight_with)
        if result == False:
            print("Game Over.")
            break
        else:
            print(r"With your foe now slain, you can progress your journey.")
            
    elif command.lower() == "help":
        print("\n")
        print("Find the secret room. Remember to check your inventory")




    
        
        

        
        











