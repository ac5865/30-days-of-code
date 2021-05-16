#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
arr = [int(x) for x in input().split(" ")]

swap = 0
for i in range(n):
    for j in range(i,n):
        if(arr[i]>arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            swap += 1
    
    if(swap==0):
        break
    
print("Array is sorted in "+str(swap) +" swaps.")
print("First Element: "+str(arr[0]))
print("Last Element: "+str(arr[n-1]))
