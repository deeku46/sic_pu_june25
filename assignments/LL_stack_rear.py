class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackRear:
    def __init__(self):
        self.head = None

    def push_rear(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def pop_rear(self):
        if self.head is None:
            print("Stack is empty")
            return
        if self.head.next is None:
            print("Popped:", self.head.value)
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        print("Popped:", current.next.value)
        current.next = None

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


stack = StackRear()

while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value to push: "))
        stack.push_rear(value)
    elif choice == 2:
        stack.pop_rear()
    elif choice == 3:
        stack.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
