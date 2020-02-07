import math
from itertools import izip
    
def get_true_start(v):

    t = int(round(v, -5))
    if t < v:
        return t + 100000

    return t

def get_true_end(v):

    t = int(round(v, -5))
    if t > v:
        return t - 100000   

    return t

def is_valid(n):

    l = str(n)
    pairs = izip(l, l[1:])

    has_double = 0

    for x in pairs:
        if x[0] > x[1]:
            return 0

        if x[0] == x[1]:
            has_double += 1

    if has_double > 0:
        return 1

    return 0

def append_manual(s, e):

    valid = 0

    for n in range(s, e + 1):

        if is_valid(n):
            valid += 1

    return valid


def combo(n):
    '''this func returns combinatorial numbers. In this case, we use 5-combinations. 
    i got this factorial-based func online'''
    return int((math.factorial(n)) / ((math.factorial(5)) * math.factorial(n - 5)))

def run(begin_start, begin_end):

    #get the nearest 100k that is higher than our start value. This may leave a remainder, which I deal with later
    start = get_true_start(begin_start)
    
    #get the nearest 100k that is lower than our end value. This may leave a remainder, which I deal with later
    end = get_true_end(begin_end)
    

    #the number of times we should calculate combinatorials
    rounds = (1000000 - max(start, 100000)) / 100000
    
    #the distance from 100k tells us which part of the combinatorial pattern we can omit
    stop = ((1000000 - min(end, 999999)) / 100000)
    
    #for the number of times the pattern should repeat, calculate combinatorials up to that number
    #becuase we are restricted to 5-combinations, we can assume that we need a minimum of 5, 5 and up to x, 5
    s = 0
    for x in range(rounds):
        s += combo(5 + x)

    #remove the combinations we didn't actually use. the pattern starts at 999k and goes down, so we remove
    #the initial patterns up to the distance from 999k
    for y in range(stop):
        s -= combo(5 + y)
        
    #Not sure why this is needed. Did tests and found this pattern as well, so I added it in
    if rounds >= 5:
        for y in range(rounds - 5):
            s -= combo(5 + y)
    
    #Take the remainders that we stripped off and calculate them manually
    s += append_manual(begin_start, start)
    s += append_manual(end, begin_end)
    
    return s
