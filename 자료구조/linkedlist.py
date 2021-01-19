class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy
        self.first_checker = 0
        self.current = None
        self.before = None

        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        
        self.tail.next = new_node
        self.tail = new_node
        self.num_of_data += 1

    def delete(self):
        
        popdata=self.current 
        if (self.current == self.tail):
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before

        self.num_of_data -= 1
        return popdata

    def first(self):
        if (self.num_of_data==0):
            return None
        self.before = self.head
        self.current = self.head.next

        self.first_checker = 1 
        return self.current.data
        
    def next(self):
        if (self.first_checker==0):
            print(" first checker is 0")
            return None
        self.before = self.current
        self.current = self.current.next
        return self.current.data

    def size(self):
        return self.num_of_data


linkedList1 = LinkedList()
linkedList1.append(3)
linkedList1.append(2)
print(linkedList1.current)
print(linkedList1.first())
print(linkedList1.num_of_data)
print(linkedList1.next())
