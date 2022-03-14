import sys

A = int(sys.stdin.readline())
A_li = list(map(int,sys.stdin.readline().split()))

for i in range(A):
    data = A_li[i]
    check = True
    if i == A-1:
        print(-1)
        break
    for j in range(i+1, A):
        if A_li[j] > data:
            print(A_li[j], end=' ')
            check = False
            break
    if check:
        print(-1,end=' ')