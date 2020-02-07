#Part 1
import numpy as np
count=0
i_arr_lst=[]
def split(word):
    return [char for char in word] 
input_="256310-732736"
bot=int(input_.split("-")[0])
top=int(input_.split("-")[1])
for i in range(bot, top+1): 
    i_str=str(i) 
    i_lst=split(i_str) 
    i_arr=np.array(i_lst) 
    is_valid_lst=[]
    
    for j in range(0,len(i_arr)):  
        if j!=5: 
            if int(i_arr[j])<=int(i_arr[j+1]): 
                is_valid=1 
            elif int(i_arr[j])>int(i_arr[j+1]): 
                is_valid=0
            is_valid_lst.append(is_valid)
    
    if len(np.unique(i_arr))==len(i_arr):
        is_valid2=0
    else:
        is_valid2=1
        
    if is_valid_lst==[1,1,1,1,1]:
        if is_valid2==1:
            count+=1
            i_arr_lst.append(i_arr)
count

#Part 2
count_2=0
for arr in i_arr_lst:
    counted_arr=np.unique(arr, return_counts=True)
    if 2 in counted_arr[1]:
        count_2+=1
count_2