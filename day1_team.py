def get_fuel(mass):
    if mass < 1: return 0
    fuel = math.floor(mass/3.0) - 2
    return fuel

def get_fuel_2(mass):
    new_fuel = 0
    x = get_fuel(mass)
    new_fuel += x
    while x > 0:
        x = get_fuel(x)
        if x < 0: continue
        new_fuel += x
    return new_fuel

def get_fuel_3(mass):
    fuel = get_fuel(mass) 
    if fuel < 1: return 0
    return fuel + get_fuel_3(fuel)


if __name__ == "__main__":
    with open('data/day1.txt') as f:
        _input = f.read()

    x = sum(map(int, _input.split('\n')[:-1]))
    print x
