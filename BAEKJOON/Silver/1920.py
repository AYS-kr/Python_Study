import sys

N = int(sys.stdin.readline())
A_li = sorted(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = map(int, sys.stdin.readline().split())

def binary_search(start,end,data):
    if start > end:
        return 0
    m = (start+end)//2
    if data == A_li[m]:
        return 1
    elif data < A_li[m]:
        return binary_search(start,m-1,data)
    else:
        return binary_search(m+1,end,data)
for _ in num:
    print(binary_search(0,len(A_li)-1,_))