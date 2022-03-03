import math
import sys

M,N = map(int, sys.stdin.readline().split())

def Prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
for i in range(M,N+1):
    if Prime_number(i):
        print(i)