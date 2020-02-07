##Part 1
def part_1(x,y):
    correct = []
    count = 0
    for num_string in range(x,y+1):
        zipped_list = list(zip(str(num_string), str(num_string)[1:]))
        if any(z[0]==z[1] for z in zipped_list) and all(z[0]<=z[1] for z in zipped_list):
            count+=1
            correct.append(num_string)
    return correct, count

#Part 2
def part_2(part_1_output_array):
    count = 0
    for num_string in part_1_output_array:
        n = ' ' + str(num_string) + ' '
        if any( n[i]==n[i+1] and n[i]!=n[i-1] and n[i+1]!=n[i+2] for i in range(1, len(n)-2)):
            count+=1
    return count


if __name__ == "__main__":
    with open('../../data/day4.txt') as _input:
        x, y = map(int, _input.read().split('-'))
    correct, count = part_1(x,y)
    print('part_1', count)
    print('part_2', part_2(correct))
