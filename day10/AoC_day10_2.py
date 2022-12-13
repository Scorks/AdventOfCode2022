import sys

def main () -> None:

    foodList = open('AoC_input_10.txt', 'r')
    lines = foodList.readlines()

    cycle = 0
    X = 1
    signal = []

    def click():
        nonlocal cycle, X, signal
        if (cycle+1) % 40 == 0:
            print('\n', end='')
        elif cycle%40 == X or cycle%40 == X-1 or cycle%40 == X+1:
            print('▓', end='')
        else:
            print('░', end='')
                
        cycle += 1


    for line in lines:
        line = line.rstrip().split(' ')

        if (line[0] == 'noop'):
            click()

        else:
            click()

            if (cycle == 20 or (cycle-20)%40 == 0):
                signal.append(cycle * X)

            click()
            
            X += int(line[1])

        if (cycle == 20 or (cycle-20)%40 == 0):
            signal.append(cycle * X)

if __name__ == '__main__':
    sys.exit(main()) 