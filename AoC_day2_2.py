foodList = open('inputs/AoC_day2_task1_input.txt', 'r')
lines = foodList.readlines()

totalScore = 0
count = 0
for line in lines:
    handScore = 0
    matchScore = 0

    opponentMove = line[0]
    myMove = line[2]

    if (opponentMove == 'A'): # rock
        if (myMove == 'X'): # you need to lose
            handScore += 3 # 3 points for choosing scissors
            matchScore += 0 # lost
        elif (myMove == 'Y'): # you need to draw
            handScore += 1 # 2 points for choosing rock
            matchScore += 3 # draw
        elif (myMove == 'Z'):
            handScore += 2 # 2 points for choosing paper
            matchScore += 6 # win
    elif (opponentMove == 'B'): # paper
        if (myMove == 'X'): # you need to lose
            handScore += 1 # 1 points for choosing rock
            matchScore += 0 # loss
        elif (myMove == 'Y'): # you need to draw
            handScore += 2 # 2 points for choosing paper
            matchScore += 3 # draw
        elif (myMove == 'Z'): # you need to win
            handScore += 3 # 3 points for choosing scissors
            matchScore += 6 # win
    elif (opponentMove == 'C'): # scissors
        if (myMove == 'X'): # you need to lose
            handScore += 2 # 2 points for choosing paper
            matchScore += 0 # loss
        elif (myMove == 'Y'): # you need to tie
            handScore += 3 # 2 points for choosing scissors
            matchScore += 3 # draw
        elif (myMove == 'Z'): # you need to win
            handScore += 1 # 1 points for choosing rock
            matchScore += 6 # win
    gameScore = handScore + matchScore
    totalScore += gameScore

print(totalScore)