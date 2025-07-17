from collections import deque
import math

class BTreeNode:
    def __init__(self, order, is_leaf):
        self.order = order
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []

    def insert_non_full(self, key):
        index = len(self.keys) - 1

        if self.is_leaf:
            self.keys.append(None)
            while index >= 0 and key < self.keys[index]:
                self.keys[index + 1] = self.keys[index]
                index -= 1
            self.keys[index + 1] = key
        else:
            while index >= 0 and key < self.keys[index]:
                index -= 1
            index += 1
            if len(self.children[index].keys) == self.order - 1:
                self.split_child(index)
                if key > self.keys[index]:
                    index += 1
            self.children[index].insert_non_full(key)

    def split_child(self, index):
        order = self.order
        full_child = self.children[index]
        new_child = BTreeNode(order, full_child.is_leaf)

        mid = order // 2
        split_key = full_child.keys[mid]

        new_child.keys = full_child.keys[mid + 1:]
        full_child.keys = full_child.keys[:mid]

        if not full_child.is_leaf:
            new_child.children = full_child.children[mid + 1:]
            full_child.children = full_child.children[:mid + 1]

        self.children.insert(index + 1, new_child)
        self.keys.insert(index, split_key)


class BTree:
    def __init__(self, order):
        self.root = BTreeNode(order, True)
        self.order = order

    def insert(self, key):
        root = self.root
        if len(root.keys) == self.order - 1:
            new_root = BTreeNode(self.order, False)
            new_root.children.append(self.root)
            new_root.split_child(0)
            self.root = new_root
        self.root.insert_non_full(key)

    def level_order_traversal(self):
        if not self.root:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            level_size = len(queue)
            level_keys = []
            for _ in range(level_size):
                node = queue.popleft()
                level_keys.extend(node.keys)
                if not node.is_leaf:
                    queue.extend(node.children)
            print(" ".join(str(k) for k in level_keys))


# Driver code
if __name__ == "__main__":
    number_of_keys, order = map(int, input().split())
    keys = list(map(int, input().split()))

    tree = BTree(order)
    for key in keys:
        tree.insert(key)

    tree.level_order_traversal()
