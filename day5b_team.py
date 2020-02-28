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
        while len(s) < 5:
            s = '0' + s

        a = x[x[pos+1]] if s[2] == '0' else x[pos+1]
        if op in [3,4]:
            return op,a,None,None
        b = x[x[pos+2]] if s[1] == '0' else x[pos+2]
        c = x[pos+3]

    return op,a,b,c
   


def intcode(_input, user_input):
    x = map(int,_input.split(','))
    i = 0
    while x[i] != 99:
        op,a,b,c = get_arguments(i,x)
        print op,a,b,c
        if op == 1:
            x[c] = a + b
            i += 4
        if op == 2:
            x[c] = a * b
            i += 4
        if op == 3:
            x[a] = user_input
            i += 2
        if op == 4:
            print x[a]
            i += 2
        if op == 5:
            i = b if int(a) != 0 else i+3
        if op == 6:
            i = b if int(a) == 0 else i+3
        if op == 7:
            x[c] = 1 if a < b else 0
            i += 4
        if op == 8:
            x[c] = 1 if a == b else 0
            i += 4

if __name__ == '__main__':
    with open('data/day5.txt') as f:
        _input = f.read()
    user_input = 5
    print intcode(_input,user_input)
