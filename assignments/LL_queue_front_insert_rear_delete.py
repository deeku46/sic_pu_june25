class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueFrontInsert:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete_rear(self):
        if self.head is None:
            print("Queue is empty")
            return
        if self.head.next is None:
            print("Deleted:", self.head.value)
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        print("Deleted:", current.next.value)
        current.next = None

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


queue = QueueFrontInsert()

while True:
    print("\n1. Insert Front\n2. Delete Rear\n3. Display\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        queue.insert_front(value)
    elif choice == 2:
        queue.delete_rear()
    elif choice == 3:
        queue.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
