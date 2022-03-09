import sys

data = list(sys.stdin.readline().strip())
cursor = len(data)
for _ in range(int(sys.stdin.readline())):
    a = list(map(str,sys.stdin.readline().split()))
    if a[0] == 'L':
        if cursor != 0:
            cursor -= 1
            
    elif a[0] == 'D':
        if cursor != len(data):
            cursor += 1
        
    elif a[0] == 'B':
        if cursor != 0 :
            del data[cursor-1]
            cursor -=1
    elif a[0] == 'P':
        data.insert(cursor, a[1])
        cursor += 1
print(''.join(data))