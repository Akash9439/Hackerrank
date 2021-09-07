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

def miniMaxSum(arr):
    # Write your code here
    newarr=sorted(arr)
    n=len(newarr)
    minsum=0
    maxsum=0
    for i in range(0,n-1):
        minsum+=newarr[i]
    
    for j in range(1,n):
        maxsum+=newarr[j]
    
    print(minsum,maxsum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
