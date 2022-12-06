foodList = open('../inputs/AoC_day3_task1_input.txt', 'r')
lines = foodList.readlines()

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

totalValue = 0

i_index = 0
j_index = 1
k_index = 2

while (k_index < len(lines)):
    elf1 = lines[i_index]
    elf2 = lines[j_index]
    elf3 = lines[k_index]

    similarity = None

    for i in elf1:
        for j in elf2:
            for k in elf3:
                if (i == j == k and i != '\n'):
                    print(i)
                    similarity = i # there should only be one of these badges

    badgeValue = (ALPHABET.index(similarity)) + 1
    totalValue += badgeValue

    i_index += 3
    j_index += 3
    k_index += 3

print(totalValue)