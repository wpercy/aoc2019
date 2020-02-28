#part1
def part_1(first,second,array):
    array[1] = first
    array[2] = second
    idx = 0
    while array[idx] != 99 and idx<= len(array):
        num = array[idx]
        val1 = array[array[idx + 1]]
        val2 = array[array[idx + 2]]
        idx3 = array[idx + 3]
        if num == 1:
            array[idx3] = val1 + val2
        elif num == 2:
            array[idx3] = val1 * val2
        idx += 4
    return array[0]



#part2
#part1
def part_2(first,second,intcode_input):
    array = intcode_input.copy()
    array[1] = first
    array[2] = second
    idx = 0
    while array[idx] != 99 and idx<= len(array):
        num = array[idx]
        val1 = array[array[idx + 1]]
        val2 = array[array[idx + 2]]
        if num == 1:
            array[array[idx + 3]] = val1 + val2
        if num == 2:
            array[array[idx + 3]] = val1 * val2
        idx += 4
    return array[0]

#combinations = [(x,y) for x in range(100) for y in range(100)]


if __name__ == "__main__":
    with open('../../data/day2.txt') as _input:
        for line in _input:
            intcode = [int(x) for x in line.split(',')]
        print(intcode)
    intcode_2 = intcode.copy()
    print("Part 1", part_1(12,2, intcode))
    print(intcode_2)
    ans = 19690720
    combinations = [(x,y) for x in range(100) for y in range(100)]
    for combo in combinations:
        #print(intcode_2)
        value = part_2(combo[0], combo[1], intcode_2)
        #print(value)
        if value == ans:
            print("Part 2", combo[0]*100+ combo[1])
