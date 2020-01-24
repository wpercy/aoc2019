print "stufft"

def intcode(_input):
    x = map(int,_input.split(','))
    x[1] = 12
    x[2] = 2
    i = 0
    while x[i] != 99 and i <= len(x):
        if x[i] == 1:
            x[x[i+3]] = x[x[i+1]] + x[x[i+2]]
        elif x[i] == 2:
            x[x[i+3]] = x[x[i+1]] * x[x[i+2]]
        i += 4
    return x[0]

def intcode_params(_input, noun, verb):
    x = map(int,_input.split(','))
    x[1] = noun
    x[2] = verb
    i = 0
    while x[i] != 99 and i <= len(x):
        if x[i] == 1:
            x[x[i+3]] = x[x[i+1]] + x[x[i+2]]
        elif x[i] == 2:
            x[x[i+3]] = x[x[i+1]] * x[x[i+2]]
        i += 4
    return x[0]

if __name__ == "__main__":
    with open('data/day2.txt') as f:
        _input = f.read()

    part1 = intcode_params(_input, 12, 2)
    print part1
    part2 = next(100*noun + verb for noun in range(100) for verb in range(100) if intcode_params(_input, noun, verb) == 19690720)
    print part2


