#!/bin/python3

import math
import os
import random
import re
import sys

def maximumToys(prices, k):
    #creating the sorted array for addition 
    arr= prices 
    
    #sorting the array 
    arr.sort()
    
    #initializing the counter 
    count=sum1=0
    
    for i in range(len(arr)-1):
    
        #if the price doesnt exceed the total amount add it to the basket count 
        if sum1+arr[i]<k:
            sum1+=arr[i]
            count+=1
    
    
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
