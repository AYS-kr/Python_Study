import sys

n = int(input())
for i in range(n):
    data = input()
    left, right = [],[]
    
    for _ in data :
        if _ == '<':
            if left:
                right.append(left.pop())
        elif _ == '>':
            if right:
                left.append(right.pop())
        elif _ == '-':
            if left:
                left.pop()
        else:
            left.append(_)
    #left + right.reverse()
    left.extend(reversed(right))
    print(''.join(left))