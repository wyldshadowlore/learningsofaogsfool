import random


class monster:
  def __init__(self, type, hp,):
    self.type = type
    self.hp = hp


p1 = monster("lazerlord", 50,)
p2 = monster("lorgling", 15, )

print(p1.type)
print(p2.type)

list1 = ['Lazerlord','lorgling']
random.choice (list1)

## what am i doing? how do i get the random choice from the list to select that monster and move t the fight phase##


hp = (mon1.hp)
print (str (hp)+" Hitpoints")


def attack(hp):
    print("Dude attacks: ")
    damage = random.randrange(1, 10, 1)
    print("Attacked for ", damage, " damage.")
    hp -= damage
    print (str(hp)+" Hitpoints")
    if hp>0:
        attack(hp)
    else:
        print ("victory achived")

attack(hp)

