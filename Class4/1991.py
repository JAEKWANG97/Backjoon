import sys


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def insert(node, parent, left_child, right_child):
    if node is None:
        return
    if node.data == parent:
        if left_child != '.':
            node.left = Node(left_child)
        if right_child != '.':
            node.right = Node(right_child)
    else:
        insert(node.left, parent, left_child, right_child)
        insert(node.right, parent, left_child, right_child)


n = int(input())
root = Node()

for _ in range(n):
    parent, left, right = input().split()
    if not root.data:
        root.data = parent
    insert(root, parent, left, right)
