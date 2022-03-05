import sys


num = list(map(int,sys.stdin.readline().split()))
sum = 0
for _ in num:
    sum += _**2
print(sum%10)