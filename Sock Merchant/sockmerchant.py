#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    c=k=0 
    for i in range (n-1):
        for j in range (i+1 , n):
            if (ar[i] is ar[j]):
                c=c+1
                ar[j]= random.randint(1,10000)
        c=c+1
        c=c-c%2
        while c>0:
            if (c%2 is 0):
                k=k+1 
                c=c-2  
        c=0  
    return k 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
