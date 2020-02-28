# DAY FIVE (helpers)
def get_arguments(pos, x):
    code = x[pos]
    if code in [3,4]:
        op = code
        a = x[pos+1]
        b = None
        c = None
    elif code <= 8:
        op = code
        a = x[x[pos+1]]
        b = x[x[pos+2]]
        c = x[pos+3]

    else:
        op = code % 100
        s = str(code)
        while len(s) < 5: s = '0' + s

        # print s

        a = x[x[pos+1]] if s[2] == '0' else x[pos+1]
        if op in [3,4]:
            return op,a,None,None
        b = x[x[pos+2]] if s[1] == '0' else x[pos+2]
        if op in [5,6]:
            return op,a,b,None
        c = x[pos+3]

    return op,a,b,c


def process(x, user_input):
    pos = 0
    while x[pos] != 99:
        # print pos, x[pos]

        op,a,b,c = get_arguments(pos, x)

        print op,a,b,c

        if op == 1:
            x[c] = a + b
            pos += 4
        elif op == 2:
            x[c] = a * b
            pos += 4
        elif op == 3:
            x[a] = user_input
            pos += 2
        elif op == 4:
            return x[a]
            # pos += 2
        elif op == 5:
            if int(a) != 0:
                pos = b
            else:
                pos += 3
        elif op == 6:
            if int(a) == 0:
                pos = b
            else:
                pos += 3
        elif op == 7:
            val = int(a < b)
            x[c] = val
            pos += 4
        elif op == 8:
            val = int(a == b)
            x[c] = val
            pos += 4


if __name__ == "__main__":
    with open('data/day5.txt') as f:
        _input = f.read()
    x = map(int, _input.split(','))
    user_input = 5 
    print process(x, user_input)
