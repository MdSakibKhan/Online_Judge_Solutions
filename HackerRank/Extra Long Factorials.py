import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n<1 or n>100 : return
    value = n-1
    result = n
    for i in range(value,1,-1):
        result = result*i;
    print(result)
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
