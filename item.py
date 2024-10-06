class Item():
    def __init__(self):
        self.name = None
        self.description = None
        # self.item_bag = []#attempt to create item bag a list that stores items, a method should check for values in the list that if there should do something

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description

    def set_description(self, item_description):
        self.description = item_description

    def describe_item(self):
        print(f"You find {self.name}. {self.description}")

    # def set_item_bag(self):
    #     self.item_bag = []

    # def add_item_bag(self):
    #     self.item_bag.append(self.name)
    #     print(f"{self.name} has been added to your inventory.")

    # def show_item_bag(self):
    #     if len(self.item_bag) == 0:
    #         print("Your bag is empty.")
    #     else:
    #         print("Player's Inventory:")
    #         for item in self.item_bag:
    #             print(f"- {self.name}")

   









