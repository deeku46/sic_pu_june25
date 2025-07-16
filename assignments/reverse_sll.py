class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse_list(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    number_of_elements = int(input("Enter number of elements: "))
    for _ in range(number_of_elements):
        element = int(input("Enter element: "))
        linked_list.insert_at_end(element)

    print("Original Linked List:")
    linked_list.display()

    linked_list.reverse_list()
    print("Reversed Linked List:")
    linked_list.display()
