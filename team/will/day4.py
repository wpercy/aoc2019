# DAY FOUR (1)
def test_value(v):
    s = str(v)
    double = False
    for i,c in enumerate(s[1:]):
        if  int(c) < int(s[i]):
            return False
        if c == s[i]:
            double = True

    return double


#valid_inputs = []
#for val in range(_range[0], _range[1]+1):
#    if test_value(val):
#        valid_inputs.append(val)

# DAY FOUR (2)
from collections import defaultdict
def test_value(v):
    s = str(v)
    double = False
    count = defaultdict(int)
    for i,c in enumerate(s[1:]):
        if  int(c) < int(s[i]):
            return False
        if c == s[i]:
            count[c] += 1

    return 1 in count.values()


if __name__ == "__main__":
    _range = [ int(x) for x in "236491-713787".split("-") ]
    valid_inputs = []
    for val in range(_range[0], _range[1]+1):
        if test_value(val):
            valid_inputs.append(val)

    print len(valid_inputs)
