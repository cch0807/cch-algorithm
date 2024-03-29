# Linked List


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third
first.value = 6


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.haed is None:
            self.head = new_node
        # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def insert_at(self, idx, value):
        current = self.head
        for _ in range(idx):
            current = current.next
        self.append(value)

    def remove(self, idx):
        pass

    def insert_back(self, value):
        pass


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)


class Linked(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
