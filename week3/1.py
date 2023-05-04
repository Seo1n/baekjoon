import sys
input = sys.stdin.readline

n = int(input())
tree = {}
# dict[root] = [left, right] == 
# tree['A'] : ['B', 'C'] A가 부모, BC가 왼쪽/ 오른쪽 자식

for i in range(n):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

#전위순회, 루트 > 왼쪽 > 오른쪽
def preorder(root):
    if root != '.':
        print(root, end= ' ')
        preorder(tree[root][0])
        preorder(tree[root][1])

#중위순회, 왼쪽 > 루트 > 오른쪽
def inorder(root):
    if root != '.':
        preorder(tree[root][0])
        print(root, end= ' ')
        preorder(tree[root][1])

#후위순회, 왼쪽 > 오른쪽 > 루트
def postorder(root):
    if root != '.':
        preorder(tree[root][0])
        preorder(tree[root][1])
        print(root, end= ' ')

preorder('A')
print()
inorder('A')
print()
postorder('A')
