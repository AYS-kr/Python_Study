import sys


T = int(input())

for _ in range(T):
    R,S = map(str,sys.stdin.readline().split())
    R = int(R)
    for i in range(len(S)):
        print(S[i]*R, end='')
    print()