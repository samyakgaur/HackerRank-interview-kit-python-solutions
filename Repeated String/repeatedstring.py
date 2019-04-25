#!/bin/python3

import math
import os
import random
import re
import sys


def repeatedString(s, n):
    #find the length of the string 
    length= len(s)
    #number of time the string will be repeated in the final string 
    #we will use the // operator here to give us the floor division 
    num=n//length
    #now we will find the remaining characters in the final string 
    #we will use the % operator as it gives the reaminder 
    rem=n%length 
    count1=0 #number of a in the repeated string 
    count2=0 #number of a in the remaining characters
    for i in range(length):
        if s[i] is 'a':
            count1+=1
        #calculating the number of times a character was repeated in the begining of 
        #of the original string 
        if s[i] is 'a' and i<rem:
            count2+=1
    total=count1*num+count2
    return total
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
