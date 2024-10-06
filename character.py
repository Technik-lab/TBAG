class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None#so each instance can do something differnent

    def describe(self):
        print(f"{self.name} is in this room.")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name}] says: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you.")
        return True


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)#we can inherit methods from super class but use our own attributes by repeating the super class attributes
        self.weakness = None#everything before below is contained in constructor class

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness#variable and value, whenever you see an = like this its a variable assignment

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend off {self.name} with the {combat_item}!!")
            return True#passes a value of true to fight without printing to terminal. so fight = true
        else:
            print(f"{self.name} crushes you, puny adventurer")
            return False

class Friend(Character):
    def __init__(self, char_name, char_description, gift):
        super().__init__(char_name, char_description)
        self.gift = None 

    def set_gift(self, gift_item):
        self.gift = gift_item#self is the instance, .gift is the method(together giving the variable), gift item is the value

    def get_gift(self):
        return self.gift

    def give_gift(self):
        print(f"{self.name} gives you {self.gift}.")
        return True


    def fight(self, combat_item):
            print(f"{self.name} doesn't want to fight with you. You will be wise to curb your thirst for combat.")
            return False

# class Player(Character): 
#     def __init__(self, char_name, char_description):
#         super().__init__(char_name, char_description)
#         self.inventory = []






