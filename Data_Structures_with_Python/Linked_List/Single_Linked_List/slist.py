#단순 연결 리스트
class Slist:
    class Node:
        def __init__(self,item,link):
            self.item = item
            self.next = link
    def __init__(self):
        self.head = None
        self.size = 0
    def size(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def insert_front(self,item):
        if self.is_empty():
            self.head = self.Node(item,None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1
    def insert_after(self,item,p):
        p.next = self.Node(item, p.next)
        self.size+=1
    def delete_front(self):
        if self.is_empty():
            #raise Exception("Underflow")
            raise EmptyError("Underflow")
        else:
            self.head = self.head.next
            self.size -= 1
            
    def delete_after(self,p):
        if self.is_empty():
            #raise Exception("Underflow")
            raise EmptyError("Underflow")
        else:
            tmp = p.next
            p.next = tmp.next
            self.size -= 1
    def search(self,target):
        p = self.head
        for i in range(self.size):
            if target == p.item:
                return i
            p = p.next
        return None
    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, ' -> ', end='')
            else:
                print(p.item)
            p = p.next
class EmptyError(Exception):
    pass
            