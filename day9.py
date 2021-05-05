#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    if(n==1):
        return 1
    else:
        return n * factorial(n-1)
    
N=int(input())
if(N<=1):
    print("1")
else:
    print(factorial(N))

