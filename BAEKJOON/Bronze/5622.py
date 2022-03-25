import sys

data = sys.stdin.readline()

d = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
answer = 0

for i in range(len(data)):
    for _ in d:
        if data[i] in _:
            answer += d.index(_) + 3

    
print(answer)