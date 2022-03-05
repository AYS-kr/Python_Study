from calendar import c
import sys

n,M = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))
sum = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] > M:
                continue
            else:
                sum = max(sum, card[i] + card[j] + card[k])

print(sum)
    