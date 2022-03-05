import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    N, M = map(int,sys.stdin.readline().split())
    que = deque(list(map(int,input().split())))
    idx_que = deque(list(0 for i in range(N)))
    
    cnt = 0
    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft()
            if idx_que.popleft() == M:
                print(cnt)
        else:
            que.append(que.popleft())
            idx_que.append(idx_que.popleft())