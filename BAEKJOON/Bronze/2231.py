N = int(input())

answer = 0
for i in range(1,N+1):
    a = list(map(int,str(i)))
    s = i + sum(a)
    if s == N :
        answer = i
        break

print(answer)