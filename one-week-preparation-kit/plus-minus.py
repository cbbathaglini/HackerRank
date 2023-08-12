#!/bin/python3

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
    positives = 0
    negatives = 0
    zeros = 0
    tam = len(arr)
    for i in range(tam):
        if arr[i] > 0: positives +=1
        elif arr[i] < 0: negatives +=1
        elif arr[i] == 0: zeros +=1
    
    print(f"{positives/tam}")
    print(f"{negatives/tam}")
    print(f"{zeros/tam}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
