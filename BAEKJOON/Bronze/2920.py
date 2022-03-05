import sys

a = list(sys.stdin.readline().split())

b = sorted(a,reverse=True)
c = sorted(a)
if a == b :
    print("descending")
elif a == c:
    print("ascending")
else:
    print("mixed")