#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Convert a 12 hr time string to 24 hr format

def timeConversion(s):
    # Write your code here
    
    arr = s.split(':')
    
    a1 = int(arr[0])
    add = s[8] + s[9]
    
    if a1==12 and add=='AM':
        a1='00'
    
    if a1!=12 and add=='PM':
        a1=12+a1
        
    str1 = str(a1).zfill(2) + ':' + arr[1] + ':' + s[6] + s[7]
    #using s[6:7] doesn't give s[6] + s[7], you have to use s[6:8]
    #but that's confusing so i did this

    return str1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
