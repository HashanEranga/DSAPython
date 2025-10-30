class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next
        return count

    def display(self):
        current = self.head
        print("printing list items")
        while current:
            print(current.data)
            current = current.next
        print("end printing list items")

    def insert_at_beginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = NewNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def insert_at_position(self, data, index):
        newNode = Node(data)
        currentPos = index
        current = self.head
        if index > 0 and index <= self.get_length():
            for i in range(currentPos - 1):
                current = current.next
            newNode.next = current.next
            current.next = newNode
        elif index < 0:
            print("Error : Position cannot be negative")
        else:
            print("Error : Position cannot exceed the current length of list")

    def delete_at_beginning(self):
        if self.head != None:
            self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, index):
        current = self.head
        if index > 0 and index <= self.get_length():
            for i in range(index - 1):
                current = current.next
            if current != None:
                current.next = current.next.next
        elif index < 0:
            print("Error : Position cannot be negative")
        else:
            print("Error : Position cannot exceed the current length of list")
