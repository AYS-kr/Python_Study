a = int(input())
b = input()
c = b[::-1]
for _ in c:
    print(a*int(_))
print(a*int(b))