#!/bin/python3

import math
import os
import random
import re
import sys

def maxCount(n):
    count=0
    while(n!=0):
        n= (n & (n << 1))
        count+=1
    return count


if __name__ == '__main__':
    n = int(input().strip())
    print(maxCount(n))
    
