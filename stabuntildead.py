import random
hp = 50
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
