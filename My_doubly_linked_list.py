class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class Doubly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        elif self.head.next == self.tail.next:
            previous_node = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.tail.prev = previous_node
        else:
            self.tail.next = new_node
            previous_node = self.tail
            self.tail = new_node
            self.tail.prev = previous_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" --> ")
            current_node = current_node.next
        print("None")

    def print_list_reverse(self):
        current_node = self.tail
        print("None", end="")
        while current_node:
            print(f" <-- {current_node.data}", end="")
            current_node = current_node.prev
        print("")

    def delete(self, data):
        if not self.head:
            raise Exception("empty list")
        elif self.head.data == data:
            next_node = self.head.next
            self.head = next_node
            self.head.prev = None
            return
        current_node = self.head
        while current_node.data != data:
            current_node = current_node.next
            if current_node.next == None:
                previous_node = current_node.prev
                previous_node.next = current_node.next
                self.tail = previous_node
                return
        previous_node = current_node.prev
        previous_node.next = current_node.next
        next_node = current_node.next
        next_node.prev = current_node.prev


ll = Doubly_Linked_List()
ll.append(10)
ll.append(24)
ll.append(30)
ll.append(50)
ll.delete(50)
ll.print_list()
ll.print_list_reverse()