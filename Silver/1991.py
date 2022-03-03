import sys

class Node:
    def __init__(self,item,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

def preorder(n):
    # 전위순회 루트,왼쪽,오른쪽
    if n!= '.':
        print(str(n.item),end='')
        if n.left != '.':
            preorder(n.left)
        if n.right != '.':
            preorder(n.right)

def inorder(n):
    # 중위순회 왼쪽, 루트, 오른쪽
    if n!= '.':
        if n.left != '.':
            inorder(n.left)
        print(str(n.item),end='')
        if n.right != '.':
            inorder(n.right)
            
def postorder(n):
    # 후위순회 왼쪽, 오른쪽, 루트
    if n != '.':
        if n.left != '.':
            postorder(n.left)
        if n.right != '.':
            postorder(n.right)
        print(str(n.item),end='')
    

n = int(input())
tree_li = []
for _ in range(n):
    data = list(map(str,sys.stdin.readline().split()))
    node = Node(data[0])
    
    node.left = data[1]
    node.right = data[2]

    tree_li.append(node)

for i in range(n):
    for j in range(n):
        if tree_li[i].item == tree_li[j].left:
            tree_li[j].left = tree_li[i]
        elif tree_li[i].item == tree_li[j].right:
            tree_li[j].right = tree_li[i]
            
preorder(tree_li[0])
print()
inorder(tree_li[0])
print()
postorder(tree_li[0])