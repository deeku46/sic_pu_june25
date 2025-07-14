class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_tree:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root  

    def height(self, root):
        if root is None:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))


bt = Binary_tree()

n = int(input("Enter number of nodes: "))
arr = list(map(int, input("Enter node values: ").split()))

root = None
for data in arr:
    root = bt.insert(root, data) 

print("Height of the tree:", bt.height(root)) 
