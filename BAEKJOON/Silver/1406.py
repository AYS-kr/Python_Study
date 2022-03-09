import sys

data_left = list(sys.stdin.readline().strip())
data_right = []

for _ in range(int(sys.stdin.readline())):
    a = list(map(str, sys.stdin.readline().split()))
    
    if a[0] == 'L':
        if data_left:
            data_right.append(data_left.pop())
        
    elif a[0] == 'D':
        if data_right:
            data_left.append(data_right.pop())
        
    elif a[0] == 'B':
        if data_left:
            data_left.pop()
            
    elif a[0] == 'P':
        data_left.append(a[1])
print(''.join(data_left + list(reversed(data_right))))