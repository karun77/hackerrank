#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    # arr=' '
    # arr = arr + strings[0]
    
    # for i in range(1,len(strings)-1):
    #     arr = arr + ' ' + strings[i]
        
    # arr = arr + ' ' + strings[len(strings)-1] + ' '
        
    # freqArr = []
    
    # for i in range(len(queries)):
    #     freqArr.append(len(re.findall(' ' + queries[i] + ' ',arr)))
    
    freqArr = [0]*len(queries)
    
    for i in range(len(strings)):
        for j in range(len(queries)):
            if strings[i]==queries[j]:
                freqArr[j] = freqArr[j]+1
            
    return freqArr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
