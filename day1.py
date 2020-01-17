# DAY ONE (1)
import math
x = map(int, _input.split('\n'))
_sum = 0
for y in x:
    _sum += (math.floor(y/3) - 2)
print _sum

# DAY ONE (2)
import math
x = map(int, _input.split('\n'))
_sum = 0
for y in x:
    new_fuel = math.floor(y/3) - 2
    _sum += new_fuel
    while new_fuel > 0:
        new_fuel = math.floor(new_fuel/3) - 2
        if new_fuel > 0:
            _sum += new_fuel
print _sum
