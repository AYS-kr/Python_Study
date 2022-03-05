import sys

T = int(input())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    li = [i for i in range(1,n+1)]
    for j in range(k):
        for l in range(1,n):
            li[l] += li[l-1]
    print(li[-1])
            
#     1    2    3   4   5
# 4 
# 3
# 2   1    4    10 20  35
# 1   1    3    6  10   15
# 0   1    2    3   4   5