import re

foodList = open('../input/AoC_input_5.txt', 'r')
lines = foodList.readlines()

stacks = [[],[],[],[],[],[],[],[],[]]

for line in lines:
    index_x = 0
    index_y = 1
    index_z = 2
    stack = 1
    if ('[' not in line):
        if ('from' in line): # the instructions
             instruction = re.findall(r'\d+', line)
             takeBoxesFromStack = stacks[int(instruction[1])-1]
             takeBoxesFromStack = takeBoxesFromStack[:int(instruction[0])]
             del stacks[int(instruction[1])-1][:int(instruction[0])]
             for item in reversed(takeBoxesFromStack):
                stacks[int(instruction[2])-1].insert(0, item)
    else:
        while (index_z < len(line)):
            box = line[index_y]
            index_x += 4
            index_y += 4
            index_z += 4
            if (box != ' '):
                stacks[stack-1].append(box)
            stack += 1


for i in stacks:
  print(i[0])
