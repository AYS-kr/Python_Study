import sys


class Stack:
    def __init__(self):
        self.st=[]
    def push(self,item):
        self.st.append(item)
    def pop(self):
        if self.isEmpty() == 0:
            return -1
        else:
            self.st.pop()
    def isEmpty(self):
        if len(self.st) == 0:
            return 0
        else :
            return 1

test_num = int(input())
for i in range(test_num):
    st = Stack()
    twice_check = 0
    test_data = list(sys.stdin.readline())
    test_data.pop()
    for j in test_data:
        if j == '(':
            st.push(j)
        else:
            if st.pop() == -1:
                print("NO")
                twice_check = 1
                break
    if st.isEmpty() == 0 and twice_check == 0:
        print("YES")
    else:
        if twice_check == 1:
            continue
        else:
            print("NO")
    