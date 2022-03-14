import sys

A = int(sys.stdin.readline())
A_li = list(map(int,sys.stdin.readline().split()))

stack = []
answer = [-1]*A

for i in range(A):
    while stack:
        if A_li[stack[-1]] < A_li[i]:
            answer[stack.pop()] = A_li[i]
        else :
            break
    stack.append(i)

print(*answer)