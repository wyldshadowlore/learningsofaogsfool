##Copy one section at a time to practice

# The basics of a function

import random  ## Import Random Module

def attack():  ## Initialize Function
    print("Dude attacks: ")  ## Print a happy line
    damage = random.randrange(1, 10, 1)  ## Randrange(Lowervalue, uppervalue, stepping)
    print("Attacked for ", damage, " damage.")  ##print the result
    
attack()

#
