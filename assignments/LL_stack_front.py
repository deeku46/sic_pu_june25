class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackFront:
    def __init__(self):
        self.top = None

    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop_front(self):
        if self.top is None:
            print("Stack is empty")
            return
        print("Popped:", self.top.value)
        self.top = self.top.next

    def display(self):
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


stack = StackFront()

while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value to push: "))
        stack.push_front(value)
    elif choice == 2:
        stack.pop_front()
    elif choice == 3:
        stack.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
