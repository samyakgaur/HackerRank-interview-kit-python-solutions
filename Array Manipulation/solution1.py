#this is not the optimized solution and hence when time is considered it may take long time to complete the task



#!/bin/python3

import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
    #where n is the number of times we need to update the list 
    # containts 3 numbers 
    result=[]
    l=k=0
    for i in range(n):
        result.append(0)
    for i in range(m):
        i1=queries[l][k]
        k+=1
        i2=queries[l][k]
        k+=1
        value=queries[l][k]
        k+=1
        for s in range(i1-1,i2):
            value1=result[s]+value
            result[s]=value1
        k=0
        l+=1
    ans=max(result)
    return ans
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
