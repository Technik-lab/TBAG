#a file where we can test our methods work without intereferring too much with our main code
from character import Enemy #import character module n enemy subclass
from character import Friend

dave = Enemy("dave", "A rotten zombie")#test. we can import subclass only as it has functionality of character class
dave.describe()
dave.set_conversation("Braaaaiiinsssss") 
dave.talk()
dave.set_weakness("cheese")
print("What will you fight with?")
fight_with = input("Enter item here: ")
dave.fight(fight_with)

goblin = Enemy("goblin", "A small green gobling, should be easy enough to take on.")
gobin.describe()
goblin.set_conversation("huh? who're you? you will not make it past me...kehkehkeeehh")
goblin.talk()
goblin.set_weakness("fire")

mariette = Friend("mariette", "A gracious elf, who seems kind.")
mariette.describe()
mariette.set_conversation("Hello traveller. You seem lost. I have something I believe will aid you.")
mariette.set_gift("key")







