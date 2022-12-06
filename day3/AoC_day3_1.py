foodList = open('../inputs/AoC_day3_task1_input.txt', 'r')
lines = foodList.readlines()

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

totalValue = 0

for line in lines:
    rucksackLength = len(line)-1
    index = int(rucksackLength/2)
    compartment1 = line[:index]
    compartment2 = line[index:]
    
    similarities = set()

    for i in compartment1:
        for j in compartment2:
            if (i == j):
                similarities.add(i)
    
    rucksackValue = 0
    for i in similarities:
        rucksackValue += (ALPHABET.index(i)) + 1

    totalValue += rucksackValue

print(totalValue)