import sys


class Queue:
    def __init__(self):
        self.q = []
    def push(self,item):
        self.q.append(item)
    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            return self.q.pop(0)
    def size(self):
        print(len(self.q))
    def empty(self):
        if len(self.q) == 0:
            return 1
        else:
            return 0
    def front(self):
        if self.empty() == 1:
            return -1
        else:
            return self.q[0]
    def back(self):
        if self.empty() == 1:
            return -1
        else:
            return self.q[-1]

test_num = int(input())
a = Queue()
for i in range(test_num):
    test_data = list(map(str,sys.stdin.readline().split()))
    if test_data[0] == 'push':
        a.push(test_data[1])
    elif test_data[0] == 'pop':
        print(a.pop())
    elif test_data[0] == 'size':
        a.size()
    elif test_data[0] == 'empty':
        print(a.empty())
    elif test_data[0] == 'front':
        print(a.front())
    elif test_data[0] == 'back':
        print(a.back())