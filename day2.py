# DAY TWO (1)
def day2(_input):
    x = map(int, _input.split(','))
    x[1] = 12
    x[2] = 2
    pos = 0
    while x[pos] != 99:
        op = x[pos]
        print op, pos
        a = x[x[pos+1]]
        b = x[x[pos+2]]
        c = x[pos+3]

        if op == 1:
            ans = a + b
        elif op == 2:
            ans = a * b

        x[c] = ans
        pos += 4
    return x[0]

def day2_again(_input):
    x = map(int, _input.split(','))
    # x[1:3] = [12,2]
    x[1] = 12
    x[2] = 2
    for i,op in enumerate(x[::4]):
        print op
        if op == 99:
            break

        pos = 4*i
        a = x[x[pos+1]]
        b = x[x[pos+2]]
        c = x[pos+3]

        if op == 1:
            ans = a + b
        elif op == 2:
            ans = a * b
        x[c] = ans

    return x[0]

# DAY TWO (2)
def day2b(_input):
    for noun in range(100):
        for verb in range(100):
            x = map(int, _input.split(','))
            x[1] = noun
            x[2] = verb
            pos = 0
            while x[pos] != 99:
                op = x[pos]
                new_pos = x[pos+3]

                a = x[x[pos+1]]
                b = x[x[pos+2]]

                if op == 1:
                    ans = a + b
                elif op == 2:
                    ans = a * b

                x[new_pos] = ans
                pos += 4
            if x[0] == 19690720:
                return (100 * noun + verb)


def day2b_again(_input):
    for noun in range(100):
        for verb in range(100):
            x = map(int, _input.split(','))
            x[1] = noun
            x[2] = verb
            pos = 0
            while x[pos] != 99:
                op = x[pos]
                new_pos = x[pos+3]

                a = x[x[pos+1]]
                b = x[x[pos+2]]

                if op == 1:
                    ans = a + b
                elif op == 2:
                    ans = a * b

                x[new_pos] = ans
                pos += 4
            if x[0] == 19690720:
                return (100 * noun + verb)

if __name__ == "__main__":
    with open('data/day2.txt') as f:
        _input = f.read()

    print day2(_input)
