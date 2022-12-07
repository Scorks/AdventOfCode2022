data = ''

with open('../inputs/AoC_input_6.txt', 'r') as file:
    data = file.read().replace('\n', '')

index_w = 0

index = None

flag = True
additionCount = -1
while(flag == True):
    letterSet = set()
    for i in range(0, 14):
        letterSet.add(data[i])
    data = data[1:]
    additionCount += 1
    if (len(letterSet) == 14):
        print(letterSet)
        flag = False
        index =additionCount + 14

print(index)

    
