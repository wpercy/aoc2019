# DAY THREE (helpers)
def get_points(w):
    points = []
    location = [0,0]
    for p in w:
        for _ in range(int(p[1:])):
            d = p[0]
            if d == 'U':
                location[1] += 1
            elif d == 'D':
                location[1] -= 1
            elif d == 'L':
                location[0] -= 1
            elif d == 'R':
                location[0] += 1
            points.append(tuple(location))

    return points

# DAY THREE (1)
def day3(_input):
    w1,w2 = _input.split('\n')
    w1,w2 = w1.split(','), w2.split(',')

    p1 = get_points(w1)
    p2 = get_points(w2)

    intersections = set(p1).intersection(set(p2))
    m = min(abs(d[0]) + abs(d[1]) for d in intersections)
    return m

# DAY THREE (2)
def day3b(_input):
    w1,w2 = _input.split('\n')
    w1,w2 = w1.split(','), w2.split(',')

    p1 = get_points(w1)
    p2 = get_points(w2)

    intersections = set(p1).intersection(set(p2))
    indices = [(p1.index(x), p2.index(x)) for x in intersections]
    m = min(x[0]+x[1] for x in indices) + 2  # +2 for zero-index

    return m

if __name__ == "__main__":
    with open('data/day3.txt') as f:
        _input = f.read()

    print day3(_input)
    print day3b(_input)
