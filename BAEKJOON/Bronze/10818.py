import sys


N = int(input())
data = list(map(int,sys.stdin.readline().split()))

print(min(data),max(data))