import sys
num = int(input())
for _ in range(num):
    a = list(map(str,sys.stdin.readline().split()))
    for i in a:
        print(i[::-1], end= ' ')
    print()