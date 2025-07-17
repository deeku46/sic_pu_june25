class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.balance(root)

    def delete(self, root, key):
        if not root:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.balance(root)

    def get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_left(self, z):
        y = z.right
        T = y.left
        y.left = z
        z.right = T
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T = y.right
        y.right = z
        z.left = T
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def balance(self, root):
        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if self.get_balance(root.left) < 0:
                root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance_factor < -1:
            if self.get_balance(root.right) > 0:
                root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


if __name__ == "__main__":
    total_nodes = int(input())
    values = list(map(int, input().split()))
    delete_key = int(input())

    avl = AVLTree()
    root = None
    for value in values:
        root = avl.insert(root, value)

    root = avl.delete(root, delete_key)
    avl.inorder(root)
    print()
