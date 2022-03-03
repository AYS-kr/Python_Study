class Dlist:
    class Node:
        def __init__(self, item,prev,link):
            self.item = item
            self.prev = prev
            self.next = link
    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None,self.head,None)
        self.head.next = self.tail
        self.size = 0
    def size(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def insert_before(self,p,item):
        t = p.prev
        n = self.Node(item,t,p)
        p.prev = n
        t.next = n
        self.size += 1
        
    def insert_after(self,p,item):
        t = p.next
        n = self.Node(item,p,t)
        t.prev = n
        p.next = n
        self.size += 1
        
    def delete(self,x):
        f = x.prev
        r = x.next
        f.next = r
        r.prev = f
        self.size -=1
        return x.item
    def print_list(self):
        if self.is_empty():
            print("리스트 비어있음")
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end='')
                else:
                    print(p.item)
                p = p.next
