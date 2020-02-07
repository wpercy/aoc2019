import pandas as pd
import math

df=pd.read_csv("Dec1.csv")

# Part One

def get_fuel(module):
    third=int(module/3)
    #third = math.floor(module/3.0) also math.ceil will round up.
    final=third-2
    return final

 final_fuel=0

 for i, row in df.iterrows():
    single_pump=0
    single_pump=get_fuel(row['Numbers'])
    final_fuel+=single_pump

 final_fuel
 #answer is 3455717

 # Part Two
 final_fuel=0

 for i, row in df.iterrows():
    single_pump=0
    single_pump=get_fuel(row['Numbers'])
    final_fuel+=single_pump
    while single_pump>6:
        single_pump=get_fuel(single_pump)
        final_fuel+=single_pump
 
final_fuel
#answer is 5180690