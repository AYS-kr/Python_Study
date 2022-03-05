import sys

num = int(input())
data_in = list(map(int,sys.stdin.readline().split()))

answer = []
student = 1
for i in data_in:
    answer.insert(i,student)
    student += 1
answer.reverse()
for i in answer:
    print(i,end=' ')