from random import randint

maxScore = 100
player0Safe = 0
player1Safe = 0

player = 0 
score = 0
safe = 0
stopping = False

# def playAgin():
#     print('Would you like to play again?')
#     print('1. Yes')
#     print('2. No')

#     choice = getInput(2)

#     if(choice == 1):
#         start()

while player0Safe < maxScore and player1Safe < maxScore:
    if(player == 0):
        safe = player0Safe
    else:
        safe = player1Safe

    print('Player:' + str(player))
    print('Safe Score:' +str(safe))
    print('Rolling Score:' +str(score))
    print()
    rolling = input('Would you like to Roll or Stay? Enter R for Roll or S for stay : ').lower()
    if rolling == 'r':
        rolledNum = randint(1, 6)
        print('Rolled ' +str(rolledNum))
        if rolledNum == 1:
            print('Bust! you lose ' + str(score) + ' but keey your previous ' + str(safe))
            stopping = True
            score = 0
        else:
            score += rolledNum
    else: 
        stopping = True

    if(stopping):
        if(player == 0):
            player0Safe += score
        else:
            player1Safe += score
        
        print()
        print('Your total score is ' +str(safe+score))
        print()
        scare = 0
        stopping = False
        player = (play+1) % 2

if(player0Safe >= maxScore):
    print('Player0 wins with a score of ' +str(player0Safe+ '!'))
else:
    print('Player0 wins with a score of ' +str(player1Safe+ '!'))
