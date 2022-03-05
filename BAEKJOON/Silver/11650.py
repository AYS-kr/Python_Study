import sys


N = int(input())
li = []
for _ in range(N):
    li.append(tuple(map(int,sys.stdin.readline().split())))

li.sort()
for _ in range(len(li)):
    print(li[_][0], li[_][1])