def new_map(func,seq): 
    mapped_seq = [] 
    for each in seq: 
        mapped_seq.append(func(each)) 
    return mapped_seq
# test new_map
import math
# x=[x for x in range(10)]
result=new_map(math.sqrt,range(10))
print(result)