#this is the optimized code and will pass all the parameters 


#!/bin/python3

import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
    vals = [0] * (n+2)
    mx = 0
    sum = 0
    for i in queries:
        vals[i[0]]+=i[2]
        vals[i[1]+1]-=i[2]
    for l in range(len(vals)):
        sum +=vals[l]
        if sum >= mx:
            mx = sum 
    return mx 
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
