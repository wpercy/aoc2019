
def fuel(mass):
    fuel = mass//3 - 2
    return fuel

def part1(input):
    return sum([fuel(x) for x in input])

def get_fuel(mass):
    y = fuel(mass)
    answer = 0
    while y>=0:
        answer += fuel(mass)
        mass = fuel(mass)
        y = fuel(mass)
    return answer

def part2(input):
    return sum([get_fuel(x) for x in input])

if __name__ == "__main__":
    input = open('../../data/day1.txt', 'r').readlines()
    input = list(map(int, input))
    print("part1", part1(input))
    print("part2", part2(input))
