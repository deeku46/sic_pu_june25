class Node:
    def __init__(self,data = ''):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")

    def search(self, value):
        temp = self.head
        count = 0
        while temp is not None:
            if value == temp.data:
                print("Element found at position ",count)
                return
            temp = temp.next
            count += 1
            print("Element not found: ")

    def delete_from_begning(self):
        temp = self.head
        if temp is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def delete_from_end(self):
        temp = self.head
        if temp is None:
            print("List is empty")
        elif temp.next is None:
            self.head = None
            return
        else:
            prev = None
            curr = self.head
            while curr.next is not None:
                prev = curr
                curr = curr.next
            prev.next = None

    def insert_at_position(self,pos,data):
        if pos == 0:
            self.insert_at_begining(data)
            return
        elif pos == len:
            self.insert_at_end(data)
        else:
            current = self.head
            count = 0
            while current is not None and count < pos - 1:
                current = current.next
                count += 1

            if current is None:
                print("Position out of bounds")
                return

            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
