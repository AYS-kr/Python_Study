import sys

N = int(sys.stdin.readline())
answer = 1
i = 0
while True:
    if N <= answer + 6 * i:
        print(i+1)
        break
    answer = answer + 6 * i
    i += 1
