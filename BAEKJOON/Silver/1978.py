import sys

N = int(sys.stdin.readline())
data = map(int, sys.stdin.readline().split())
count = 0

for i in data:
    if i == 1:
        continue
    for _ in range(2,i):
        if i % _ == 0:
            break
    else:
        count += 1
        
print(count)