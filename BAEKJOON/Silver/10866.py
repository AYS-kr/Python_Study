from collections import deque
import sys
def push_front(data):
    deque.appendleft(data)

def push_back(data):
    deque.append(data)

def pop_front():
    if deque:
        print(deque.popleft())
    else:
        print(-1)

def pop_back():
    if deque:
        print(deque.pop())
    else:
        print(-1)

def size():
    print(len(deque))

def empty():
    if deque:
        print(0)
    else:
        print(1)

def front():
    if deque:
        print(deque[0])
    else:
        print(-1)

def back():
    if deque:
        print(deque[-1])
    else:
        print(-1)
        
deque = deque()
for _ in range(int(sys.stdin.readline())):
    data = list(map(str,sys.stdin.readline().split()))
    if data[0] == 'push_front':
        push_front(data[1])
    elif data[0] == 'push_back':
        push_back(data[1])
    elif data[0] == 'pop_front':
        pop_front()
    elif data[0] == 'pop_back':
        pop_back()
    elif data[0] == 'size':
        size()
    elif data[0] == 'empty':
        empty()
    elif data[0] == 'front':
        front()
    elif data[0] == 'back':
        back()
