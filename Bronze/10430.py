import sys


A,B,C = list(map(int,sys.stdin.readline().split()))

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)