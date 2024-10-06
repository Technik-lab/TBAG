from item import Item 


cheese = Item()
cheese.set_name("cheese")
cheese.set_description("Just a slice. Great for sandwiches, weirdly even better for killing zombies.")
cheese.describe_item()

bag = Item()
bag.set_item_bag()
bag.add_item_bag()
bag.show_item_bag()
