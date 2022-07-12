import random
import time


def getAnswer(choice):
    if choice == 1:
       print('It Is Certain')
    elif choice == 2:
        print('Without A Doubt')
    elif choice == 3:
        print('Yes - Definitely')
    elif choice == 4:
        print('You May Rely On It')
    elif choice == 5:
        print('As I See It, Yes')
    elif choice == 6:
        print('Most Likely')
    elif choice == 7:
        print('Outlook Good')
    elif choice == 8:
        print('Yes')
    elif choice == 9:
        print('Signs Point To Yes')
    elif choice == 10:
        print('Reply Hazy, Try Again')
    elif choice == 11:
        print('Ask Again Later')
    elif choice == 12:
        print('Better Not Tell You Now')
    elif choice == 13:
        print('Cannot Predict Now')
    elif choice == 14:
        print('Concentrate And Ask Again')
    elif choice == 15:
        print('Do Not Count On It')
    elif choice == 16:
        print('My Reply Is No')
    elif choice == 17:
        print('My Sources Say No')
    elif choice == 18:
        print('Outlook Not So Good')
    elif choice == 19:
        print('No')
    elif choice == 20:
        print('Very doubtful.')


getAnswer(random.randint(1,20))


