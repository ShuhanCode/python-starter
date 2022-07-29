import time
import random
def displayintro():
    print ("you are inside the confines of roblox and you see 2 chests")
    print ("one chest has 1,000, 000, robux")
    print ("the other has a thirsty femboy rat")
    print ()

def choosechest () :
    chest = ""
    while chest !="1" and chest != "2":
        print ("which chest big boy? one or two")
        chest = input ()
    return chest
def Checkchest(chosenchest) :
    print ("you approch a chest...")
    time.sleep (2)
    print ("BLEGH IT SMEELS SO000 BAD")
    time.sleep (4)
    print ("creeeeeeeeeeeek...'' ")
    print ()
    goodchest = random.randint (1.2)

    if chosenchest == str(goodchest) :
        print ("youre richer than linkmon99 man! ")
    else:
        print ("slurpy slupry i want ur cheese daddy uwu nuzzle nuzzle >:3")

playagain = "yes"

while playagain =="yes" or playagain == "y":
    print ("what u wanna play again?")

    displayintro()

    chestNumber = choosechest()

    Checkchest(chestNumber)

    print ("Do you want to play again?")
    (yes or no)
    playagain = input()


