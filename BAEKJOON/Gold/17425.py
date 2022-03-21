# python으로는 시간초과
# PyPy3로는 통과
# ?!?!?!? 음... 아직까지 이유는 모르겠음.

import sys
# 최댓값 100만
answer = [0 for _ in range(1000001)]
for i in range(1,1000001):
    for j in range(i,1000001,i):
        answer[j] += i
    answer[i] += answer[i-1]

for i in range(int(sys.stdin.readline())):
    data = int(sys.stdin.readline())
    print(answer[data])