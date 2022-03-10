import sys

data = list(sys.stdin.readline().rstrip())
count = 0
stack = []
for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    else:
        # 레이저 이니깐 더하기
        if data[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
            
print(count)