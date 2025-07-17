class Node:
    def __init__(self, value):
        self.value = value
        self.color = 'R'
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = 'B'
        self.root = self.NIL

    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.parent = None

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'R'
        self.fix_insert(new_node)

    def left_rotate(self, node):
        right = node.right
        node.right = right.left
        if right.left != self.NIL:
            right.left.parent = node
        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

    def right_rotate(self, node):
        left = node.left
        node.left = left.right
        if left.right != self.NIL:
            left.right.parent = node
        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        left.right = node
        node.parent = left

    def fix_insert(self, node):
        while node.parent and node.parent.color == 'R':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'B'

    def in_order(self, node, result):
        if node != self.NIL:
            self.in_order(node.left, result)
            result.append(f"{node.value}({node.color})")
            self.in_order(node.right, result)

tree = RedBlackTree()
n = int(input())
values = list(map(int, input().split()))
for value in values:
    tree.insert(value)
result = []
tree.in_order(tree.root, result)
print(' '.join(result))
