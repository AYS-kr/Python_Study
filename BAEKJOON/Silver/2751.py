import sys

data = []

for _ in range(int(sys.stdin.readline())):
    data.append(int(sys.stdin.readline()))

data.sort()

print('\n'.join(str(i) for i in data))