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
    n=len(arr)
    pos=0
    neg=0
    zero=0
    for i in range(0,n):
        if(arr[i]>0):
            pos+=1
        elif(arr[i]<0):
            neg+=1
        else:
            zero+=1
    posr=float(pos/n)
    negr=float(neg/n)
    zeror=float(zero/n)
    print(format(posr,".6f"))
    print(format(negr,".6f"))
    print(format(zeror,".6f"))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
