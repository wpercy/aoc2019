def run(start, end):
    
    from itertools import izip
    
    def get_true_start(s):

        nums = [int(x) for x in str(s)]

        prev = 0
        true = ""
        count = 0

        for x in nums:
            if x > prev:
                true = true + str(x)
                prev = x
                count += 1

            else:
                return int(true + (str(prev) * (len(nums) - count)))
            
    def get_true_end(s):

        nums = [int(x) for x in str(s)]

        prev = 0
        true = ""
        count = 0

        for x in nums:
            if x > prev:
                true = true + str(x)
                prev = x
                count += 1

            else:
                return int(true[:-1] + str(int(true[-1:]) - 1) + ("9" * (len(nums) - count)))  
            
    def is_valid(n):

        l = str(n)
        pairs = izip(l, l[1:])

        has_double = 0

        for x in pairs:
            if x[0] > x[1]:
                return 0

            if x[0] == x[1] and has_double == 1:
                return 0

            if x[0] == x[1]:
                has_double = 1

        if has_double == 1:
            return 1

        return 0
    
    def iterate(s, e):

        valid = 0

        for n in range(s, e + 1):

            if is_valid_part2(n):
                valid += 1

        return valid
    
    s = get_true_start(start)
    e = get_true_end(end)
    
    valid = iterate(s, e)
    
    return valid
    
run(178416, 676461)
