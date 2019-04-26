#!/bin/python3

import math
import os
import random
import re
import sys


def minimumSwaps(arr):
    swaps=0
    for i in range(0, n - 1):
        while arr[i] != i + 1:              //is number equal to its index eq is '2' == index 2(1+1)
            t = arr[arr[i] - 1]             //store the data in the index arr[number-1]
            arr[arr[i] - 1] = arr[i]        //assign the data in the wrong index to the index just 1 less than its value
            arr[i] = t                      //restore the destroyed number
            swaps += 1
    return swaps  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
