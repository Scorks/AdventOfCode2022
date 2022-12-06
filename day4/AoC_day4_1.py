foodList = open('../inputs/AoC_day4_task1_input.txt', 'r')
lines = foodList.readlines()

totalOverlap = 0

for line in lines:
    x = line.rstrip().split(",")
    elf1_bounds = x[0].split("-")
    elf2_bounds = x[1].split("-")

    if ((int(elf1_bounds[0]) >= int(elf2_bounds[0])) and (int(elf1_bounds[1]) <= int(elf2_bounds[1]))):
        totalOverlap += 1
    elif ((int(elf2_bounds[0]) >= int(elf1_bounds[0])) and (int(elf2_bounds[1]) <= int(elf1_bounds[1]))):
        totalOverlap += 1
    
print(totalOverlap)