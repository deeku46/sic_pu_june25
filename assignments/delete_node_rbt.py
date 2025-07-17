class Node:
    def __init__(self, data, color):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NULL = Node(0, 'B')
        self.NULL.left = self.NULL.right = self.NULL.parent = self.NULL
        self.root = self.NULL

    def level_order(self):
        result = []
        colors = []
        if self.root == self.NULL:
            return result, colors
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            colors.append(node.color)
            if node.left != self.NULL:
                queue.append(node.left)
            if node.right != self.NULL:
                queue.append(node.right)
        return result, colors

    def insert_level_order(self, keys, colors):
        if not keys:
            return
        nodes = [Node(keys[i], colors[i]) for i in range(len(keys))]
        for node in nodes:
            node.left = self.NULL
            node.right = self.NULL
            node.parent = self.NULL
        self.root = nodes[0]
        queue = [self.root]
        index = 1
        while queue and index < len(nodes):
            current = queue.pop(0)
            if index < len(nodes):
                current.left = nodes[index]
                nodes[index].parent = current
                queue.append(nodes[index])
                index += 1
            if index < len(nodes):
                current.right = nodes[index]
                nodes[index].parent = current
                queue.append(nodes[index])
                index += 1

    def transplant(self, u, v):
        if u.parent == self.NULL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def delete_node(self, data):
        z = self.search_tree(self.root, data)
        if z == self.NULL:
            return
        y = z
        y_original_color = y.color
        if z.left == self.NULL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'B':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'B':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'R':
                    s.color = 'B'
                    x.parent.color = 'R'
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == 'B' and s.right.color == 'B':
                    s.color = 'R'
                    x = x.parent
                else:
                    if s.right.color == 'B':
                        s.left.color = 'B'
                        s.color = 'R'
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 'B'
                    s.right.color = 'B'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'R':
                    s.color = 'B'
                    x.parent.color = 'R'
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.left.color == 'B' and s.right.color == 'B':
                    s.color = 'R'
                    x = x.parent
                else:
                    if s.left.color == 'B':
                        s.right.color = 'B'
                        s.color = 'R'
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 'B'
                    s.left.color = 'B'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'B'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NULL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NULL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search_tree(self, node, key):
        if node == self.NULL or key == node.data:
            return node
        if key < node.data:
            return self.search_tree(node.left, key)
        return self.search_tree(node.right, key)

def run_rbt_delete():
    N = int(input())
    keys = list(map(int, input().split()))
    colors = input().split()
    key_to_delete = int(input())
    rbt = RedBlackTree()
    rbt.insert_level_order(keys, colors)
    rbt.delete_node(key_to_delete)
    order, color_order = rbt.level_order()
    print(" ".join(map(str, order)))
    print(" ".join(color_order))

run_rbt_delete()
