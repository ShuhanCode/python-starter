import random
import time
from random import randint

choice = random.randint(1,20)

def getAnswer(choice):
    if choice == 1:
        print('It is certain.')
    elif choice == 2:
        print('It is decidedly so.')
    elif choice == 3:
        print('Without a doubt.')
    elif choice == 4:
        print('Yes definitely.')
    elif choice == 5:
        print('You may rely on it.')    
    elif choice == 6:
        print('As I see it, yes.')
    elif choice == 7:
        print('Most likely.')
    elif choice == 8:
        print('Outlook good.')
    elif choice == 9:
        print('Yes.')
    elif choice == 10:
        print('Signs point to yes.')
    elif choice == 11:
        print('Reply hazy, try again.')
    elif choice == 12:
        print('Ask again later.')
    elif choice == 13:
        print('Better not tell you now..')
    elif choice == 14:
        print('Cannot predict now.')
    elif choice == 15:
        print('Concentrate and ask again.')
    elif choice == 16:
        print("Don't count on it.")
    elif choice == 17:
        print('My reply is no.')
    elif choice == 18:
        print('My sources say no.')
    elif choice == 19:
        print('Outlook not so good.')
    elif choice == 20:
        print('Very doubtful.')

