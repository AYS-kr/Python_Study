import sys


num = int(input())

for _ in range(num):
    H,W,N = map(int,sys.stdin.readline().split())
    for i in range(1, W+1):
        for j in range(1, H+1):
            N -= 1
            if N == 0:
                print("{0}{1:02}".format(j,i))
            