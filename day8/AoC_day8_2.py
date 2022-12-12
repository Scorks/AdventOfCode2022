# reading input in as 2-D array
with open("AoC_input_8.txt") as textFile:
        lines = [line.split() for line in textFile]


for i in range(0, len(lines)):
    lst = []
    for letter in lines[i][0]:
        lst.append(letter)
    lines[i] = lst

visibleTrees = 0
maxVisibilityScore = 0
visibilityScore = []

for i in range(0, len(lines)):
    visibilityScore.append([]) # storing values for part two

count = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if (i == 0 or j == 0 or i == len(lines)-1 or j == len(lines[0])-1):
            visibilityScore[i].append(0)
            visibleTrees += 1
        else:
            c_left = False
            c_right = False
            c_up = False
            c_down = False

            score = 0

            count_left = 0
            count_right = 0
            count_up = 0
            count_down = 0

            for k in range(j-1, -1, -1): # look at the rows
                count_left += 1
                if (lines[i][k] >= lines[i][j]):
                    score = count_left
                    c_left = True
                    break
            if (c_left == False):
                score = count_left
            for k in range(j+1, len(lines[0])):
                count_right += 1
                if (lines[i][k] >= lines[i][j]):
                    score = score * count_right
                    c_right = True
                    break
            if c_right == False:
                score = score * count_right
            for k in range(i-1, -1, -1): # look at the columns
                count_up += 1
                if (lines[k][j] >= lines[i][j]):
                    score *=  count_up
                    c_up = True
                    break
            if c_up == False:
                score = score * count_up
            for k in range(i+1, len(lines)):
                count_down += 1
                if (lines[k][j] >= lines[i][j]):
                    score = score * count_down
                    c_down = True
                    break
            if c_down == False:
                score = score * count_down

            if (score >= maxVisibilityScore):
                maxVisibilityScore = score
            if(not(c_left == True and c_right == True and c_up == True and c_down == True)):
                visibleTrees += 1
               
print(maxVisibilityScore)