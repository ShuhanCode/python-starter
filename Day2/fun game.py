choice = -1


def getInput(choices):
    while True:
        num = input()


        try:
            num = int(num)
        except:
            print('Please enter a number')
        else:
            if(num > 0 and num < choices+1):
                return num
            else:
                print('Please enter a number between 1 and ' + str(choices))
def playAgain():
    print('Would you like to play again?')
    print('1. Yes')
    print('2. No')

    Choice = getInput(2)


    if(choice == 1):
        start()
def start():
    print('You are walking in the forest and you come accross a snake. What will you do?')


    print('1. Go around the snake')
    print('2. Run away')
    print('3. Climb a tree')

    choice = getInput(3)

    if(choice == 1):
        print('You escape the snake becuase it was not poisonous! Now it starts to rain. Where should you find shelter?')
    
        print('1. In a cave')
        print('2. Build shelter')
        print('3. Find shelter')
     
    elif(choice == 2):
        print("A bear chases you. You die!")
        print('Bad ending!!!')
        playAgain()


    elif(choice == 3):
        print("A bear climbs behind you. You die!")
        print('Bad ending!!!')
        playAgain()

 
    
