foodList = open('../inputs/AoC_day1_task1_input.txt', 'r')
lines = foodList.readlines()

highestCalorieCount = [0, 0, 0]
currentCalorieCount = 0

def checkIfHigherThanMinimumValueInList(value, list):
    minValue = min(list)
    minIndex = list.index(minValue)
    if (value > minValue):
        list[minIndex] = value
    return list
    
for line in lines:
    if line.strip(): # the line is not empty
        currentCalorieCount += int(line)
    else: # line is empty
        highestCalorieCount = checkIfHigherThanMinimumValueInList(currentCalorieCount, highestCalorieCount)
        currentCalorieCount = 0
total = sum(highestCalorieCount)

print(highestCalorieCount)
print(total)