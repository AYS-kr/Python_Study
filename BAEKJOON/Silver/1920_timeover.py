import sys

N = int(sys.stdin.readline())
A_li = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

for _ in num:
    if _ in A_li:
        print(1)
    else:
        print(0)