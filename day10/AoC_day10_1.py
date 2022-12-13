import sys

def main () -> None:

    foodList = open('AoC_input_10.txt', 'r')
    lines = foodList.readlines()

    cycle = 1
    X = 1
    signal = []


    for line in lines:
        line = line.rstrip().split(' ')

        if (line[0] == 'noop'):
            cycle += 1

        else:
            cycle += 1

            if (cycle == 20 or (cycle-20)%40 == 0):
                signal.append(cycle * X)

            cycle += 1
            
            X += int(line[1])

        if (cycle == 20 or (cycle-20)%40 == 0):
            signal.append(cycle * X)

    print(sum(signal))

if __name__ == '__main__':
    sys.exit(main()) 