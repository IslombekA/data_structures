
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if not self.head:
            raise Exception("list is empty")
        if index <= 1:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for i in range(index - 2):
            if current_node.next:
                current_node = current_node.next
            else:
                raise Exception(f"{index} is above the index threshold")
        new_node.next = current_node.next
        current_node.next = new_node

    def insert(self, data, before_data):
        new_node = Node(data)
        if not self.head:
            raise Exception("list is empty")
        if self.head.data == before_data:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next and current_node.next.data != before_data:
            current_node = current_node.next
        if current_node.next == None:
            raise Exception(f"{before_data} does not exist in the list")
        new_node.next = current_node.next
        current_node.next = new_node
    
    def insert2(self, data, after_data):
        new_node = Node(data)
        if self.head.data == after_data:
            new_node.next = self.head.next
            self.head.next = new_node
            return  
        current_node = self.head
        while current_node.next and current_node.next.data != after_data:
            current_node = current_node.next
        if current_node.next.data == after_data:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node        

    def delete(self, data):
        if not self.head:
            raise Exception("List is empty")
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = current_node.next
        current_node = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(24)
linked_list.append(30)
linked_list.prepend(5)
linked_list.prepend(25)
linked_list.print_list()