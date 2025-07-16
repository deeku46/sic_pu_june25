class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element
        print(f"{element} enqueued.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"{removed} dequeued.")

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue contents:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

if __name__ == "__main__":
    queue_size = int(input("Enter queue size: "))
    queue = CircularQueue(queue_size)

    while True:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            element = input("Enter element to enqueue: ")
            queue.enqueue(element)
        elif choice == "2":
            queue.dequeue()
        elif choice == "3":
            queue.display()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
