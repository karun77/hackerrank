#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    
    #we could use a dictionary instead of 99 element array to store 
    #the number of occurences of an integer
    
    intDict = {}
    lonelyInt=0
    
    for i in range(len(a)):
        if dict.__contains__(intDict,a[i])==False:
            intDict[a[i]]=1
            lonelyInt = lonelyInt+a[i]
        else:
            intDict[a[i]]=intDict[a[i]]+1
            lonelyInt = lonelyInt - a[i]
    
    return lonelyInt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
