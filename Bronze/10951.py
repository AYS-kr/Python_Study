import sys

num = list(map(int,sys.stdin.readline().split()))
while num:
    print(sum(num))
    num = list(map(int,sys.stdin.readline().split()))