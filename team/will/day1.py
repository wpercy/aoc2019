# DAY ONE (1)
import math
def day1a(_input):
    x = map(int, _input.split('\n'))
    _sum = 0
    for y in x:
        _sum += (math.floor(y/3) - 2)
    return _sum

# DAY ONE (2)
import math
def day1b(_input):
    x = map(int, _input.split('\n'))
    _sum = 0
    for y in x:
        new_fuel = math.floor(y/3) - 2
        _sum += new_fuel
        while new_fuel > 0:
            new_fuel = math.floor(new_fuel/3) - 2
            if new_fuel > 0:
                _sum += new_fuel
    return _sum


if __name__ == "__main__":
    with open('data/day1.txt') as f:
        i = f.read()
    print day1a(i)
