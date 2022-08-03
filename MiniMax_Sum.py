#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# print minimum and maximum sum of 4/5 elements in given array

def miniMaxSum(arr):
    # Write your code here
    
    array1 = [0]*len(arr)
    
    for x in range(len(arr)):
        array1[x] = arr[x]
    
    #a sorting algorithm
    
    for i in range(len(array1)-1):
        s = array1[i]
        for j in range(i+1,len(array1)):
            if array1[j]<array1[i]:
                s=array1[j]
                array1[j]=array1[i]
                array1[i]=s        
    
    #then min and max sum is easily calculated
    minX = sum(array1[0:(len(array1)-1)])
    maxX = sum(array1[1:(len(array1))])
    
    print(str(minX) + ' ' + str(maxX))
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
