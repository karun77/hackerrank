import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    cp=0;
    nZeros=0;

    for i in arr:
        if i*(-1)<0:
            cp=cp+1
        if i==0:
            nZeros=nZeros+1
            
    a=cp/len(arr)
    b=(len(arr) - cp - nZeros)/len(arr)
    c=nZeros/len(arr)
    print('%.6f'%a)
    print('%.6f'%b)
    print('%.6f'%c)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
