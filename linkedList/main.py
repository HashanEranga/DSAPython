from LinkedList import LinkedList

l_list = LinkedList()

# print nodes in an empty list
l_list.print_nodes_list()

# insert a node at the front of the list
l_list.insert_at_front(12)
l_list.insert_at_front(234)
l_list.insert_at_front(345)

# print nodes in the list
print("printing the list")
l_list.print_nodes_list()

# insert a node at the end of the list
l_list.insert_at_end_efficient(232)
l_list.insert_at_end_efficient(567)
l_list.insert_at_end_efficient(532)

# print nodes in the list again
print("printing the list")
l_list.print_nodes_list()

print("printing the list to test insert at kth position")
l_list.insert_at_front(5)
l_list.insert_at_k(1234, 2)
l_list.print_nodes_list()
