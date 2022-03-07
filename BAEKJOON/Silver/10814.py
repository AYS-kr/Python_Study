import sys


li =[]
for _ in range(int(sys.stdin.readline())):
    age, name = map(str,sys.stdin.readline().split())
    age = int(age)
    li.append((age, name))

# 첫 인덱스에 있는 숫자만 보면 정렬
li.sort(key= lambda x : x[0])

for _ in li:
    print(_[0],_[1])