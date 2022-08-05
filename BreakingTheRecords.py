#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

# return the count of times minimum and maximum record is broken (the record
# is established at the first game)

def breakingRecords(scores):
    # Write your code here
    
    flag=1
    minCount=0
    maxCount=0
    
    for i in range(len(scores)):
        if flag:
            min1=scores[i]
            max1=scores[i]
            flag=0
            continue
        if scores[i]>max1:
            max1 = scores[i]
            maxCount = maxCount+1
        if scores[i]<min1:
            min1 = scores[i]
            minCount = minCount+1
    
    arr = [maxCount,minCount]       
    
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
