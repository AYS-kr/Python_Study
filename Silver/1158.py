test_data = list(map(int, input().split()))
round = []
for i in range(test_data[0]):
    round.append(i+1)
    
answer = []
num = 0
for i in range(test_data[0]):
    num += test_data[1] -1
    if num >= len(round):
        num %= len(round)
    answer.append(round.pop(num))

print("<",end='')
for i in range(len(answer)-1):
    print("{}, ".format(answer[i]), end='')
print(answer[-1],end='')
print(">")