import sys

class Stack:
    def __init__(self):
        self.top = []
    def push(self,item):
        self.top.append(item)    
    def pop(self):
        if self.isEmpty() == 0:
            return print(self.top.pop(-1))
        else:
            return print('-1')
    def size(self):
        print(len(self.top))
    def isEmpty(self):
        if len(self.top) == 0:
            #비어있는 상태
            return 1
        else:
            return 0
    def is_top(self):
        if self.isEmpty() == 1:
            print('-1')
        else:
            print(self.top[-1])
            
        
a = Stack()
testcase_num = int(input())
for i in range(testcase_num):
    data_in = list(map(str,sys.stdin.readline().split()))
    if data_in[0] == "push":
        a.push(data_in[1])
    elif data_in[0] == "pop":
        a.pop()
    elif data_in[0] == "size":
        a.size()
    elif data_in[0] == "empty":
        print(a.isEmpty())
    elif data_in[0] == "top":
        a.is_top()