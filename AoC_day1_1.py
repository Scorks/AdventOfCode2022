foodList = open('inputs/AoC_day1_task1_input.txt', 'r')
lines = foodList.readlines()

bestElf = None
highestCalorieCount = 0
currentCalorieCount = 0

elfIndex = 1

for line in lines:
    if line.strip(): # the line is not empty
        currentCalorieCount += int(line)
    else:
        if (currentCalorieCount > highestCalorieCount):
            highestCalorieCount = currentCalorieCount
            bestElf = elfIndex
        currentCalorieCount = 0
        elfIndex += 1

print(highestCalorieCount)