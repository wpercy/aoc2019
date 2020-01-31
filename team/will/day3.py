class Wire(object):

    def __init__(self, directions):
        directions = directions.split(',')
        self.points = self.get_points(directions)

    def get_points(self, directions):
        points = []
        location = [0,0]
        for p in directions:
            d = p[0]
            for _ in range(int(p[1:])):
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

    def get_intersections(self, wire):
        intersections = set(self.points).intersection(set(wire.points))
        return intersections


if __name__ == "__main__":
    with open('data/day3.txt') as f:
        _input = f.read()

    wires = _input.strip().split('\n')
    
    w1 = Wire(wires[0])
    w2 = Wire(wires[1])

    intersections = w1.get_intersections(w2)
    m = min(abs(d[0]) + abs(d[1]) for d in intersections)
    print m
    indices = [(w1.points.index(x), w2.points.index(x)) for x in intersections]
    mm = min(x[0]+x[1] for x in indices) + 2  # +2 for zero-index
    print mm
