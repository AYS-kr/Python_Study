N,X = map(int,input().split())

A = list(map(int,input().split()))

for _ in A:
    if _ < X:
        print(_,end=' ')
print()