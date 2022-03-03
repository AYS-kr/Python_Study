import sys


num = list(map(int,sys.stdin.readline().split()))

while sum(num) != 0:
    print(sum(num))
    num = list(map(int,sys.stdin.readline().split()))