def run_part1(start, end):
    
    import math
    
    rounds = (1000000 - max(start, 100000)) / 100000
    stop = ((1000000 - min(end, 999999)) / 100000)
    
    #thanks to an online tutorial for this func
    def combo(n, r):
        return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

    s = 0
    for x in range(rounds):
        s += combo(5 + x, 5)

    #distance from 100k
    for y in range(stop):
        s -= combo(5 + y, 5)
        
    #don't know why i need this but I realized i did...
    if rounds >= 5:
        for y in range(rounds - 5):
            s -= combo(5 + y, 5)
    
    return s
    
run_part1(100000, 999999)
