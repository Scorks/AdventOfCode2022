# reading input in as 2-D array
with open("AoC_input_8.txt") as textFile:
        lines = [line.split() for line in textFile]


for i in range(0, len(lines)):
    lst = []
    for letter in lines[i][0]:
        lst.append(letter)
    lines[i] = lst

visibleTrees = 0

count = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if (i == 0 or j == 0 or i == len(lines) or j == len(lines[0])):
            visibleTrees += 1
        else:
            c_left = False
            c_right = False
            c_up = False
            c_down = False
            for k in range(0, j): # look at the rows
                if (lines[i][k] >= lines[i][j]):
                    c_left = True
            for k in range(j+1, len(lines[0])):
                if (lines[i][k] >= lines[i][j]):
                    c_right = True
            for k in range(0, i): # look at the columns
                if (lines[k][j] >= lines[i][j]):
                    c_up = True
            for k in range(i+1, len(lines)):
                if (lines[k][j] >= lines[i][j]):
                    c_down = True
            if(not(c_left == True and c_right == True and c_up == True and c_down == True)):
                visibleTrees += 1
               
print(visibleTrees)