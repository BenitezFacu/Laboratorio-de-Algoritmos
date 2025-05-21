import os, random
os.system('cls')

class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)
    
die_6 = Die(6)

print("10 números del 1-5")
for a in range(10):
    print(die_6.roll_die())

die_10 = Die(10)

print("10 números del 1-10")
for a in range(10):
    print(die_10.roll_die())

die_20 = Die(20)

print("10 números del 1-20")
for a in range(10):
    print(die_20.roll_die())