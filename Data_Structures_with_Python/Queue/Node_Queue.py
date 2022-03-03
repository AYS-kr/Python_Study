class Node:
    def __init__(self,item,n):
        self.item = item
        self.next = n

def add(item):
    global size
    global front
    global rear
    new_node = Node(item,None)
    if size == 0:
        front = new_node
    else:
        rear.next = new_node
    rear = new_node
    size += 1

def remove():
    global size
    global front
    global rear
    if size!= 0:
        fitem = front.item
        front = front.next
        size -=1
        if size == 0:
            rear = None
        return fitem

def print_q():
    p = front
    print('front -> ', end='')
    while p:
        if p.next != None:
            print(p.item, '->  ', end='')
        else:
            print(p.item, end ='')
        p = p.next
    print(' :rear')

front=None
rear = None
size= 0
add('apple')
add('orange')
add('cherry')
add('pear')
print("사과, 오렌지, 체리, 배 삽입 후: \t")
print_q()
remove()
print('remove한 후:\t\t')
print_q()
remove()
print('remove한 후:\t\t')
print_q()
add('grape')
print('포도 삽입 후"\t\t')
print_q()