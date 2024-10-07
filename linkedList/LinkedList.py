from Node import Node

class LinkedList:
    # initialize a linked list
    def __init__(self):
        self.head = None

    def insert_at_front(self, value):
        # 1. create a new node
        new_node = Node(value)

        # 2. make the new node point to the current head
        new_node.next = self.head

        # 3. make the new node the head
        self.head = new_node

    def insert_at_end(self, value):
        # 1. create a new node
        new_node = Node(value)

        # 2. if the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node

        # 3. otherwise, traverse the list to the last node
        current_node = self.head

        # 4. make the last node point to the new node
        while current_node.next:
            current_node = current_node.next

        # 5. make the new node the last node
        current_node.next = new_node

    def get_head_value(self):
        # 1. if the list is not empty, return the value of the head
        if self.head is not None:
            return self.head.value
        # 2. otherwise, return -1
        else:
            return -1

    def get_end_value(self):
        # 1. if the list is empty, return
        if self.head is None:
            return -1
        # 2. otherwise, traverse the list to the last node
        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            return current_node.value

    def print_nodes_list(self):
        # if the list is empty, return
        if self.head is None:
            print("linked list is empty")
        # otherwise, traverse the list and print the value of each node
        else:
            current_node = self.head

            while current_node:
                print(f"Node value : {str(current_node.value)}")
                current_node = current_node.next






