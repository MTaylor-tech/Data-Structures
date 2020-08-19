class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        self.add_to_tail(value)

    def add_to_tail(self, value):
        new_node = Node(value)
        self.add_node_to_tail(new_node)
        self.length += 1

    def add_node_to_tail(self, node):
        if self.tail is not None:
            self.tail.next = node
        else:
            self.add_node_to_head(node)
        self.tail = node

    def add_node_to_head(self, node):
        if self.head is not None:
            node.next = self.head
        self.head = node

    def add_to_head(self, value):
        new_node = Node(value)
        self.add_node_to_head(new_node)
        self.length += 1

    def remove_head(self):
        value = None
        old_head = self.head
        if old_head is not None:
            if self.tail is old_head:
                self.tail = None
            if old_head.next is not None:
                self.head = old_head.next
            else:
                self.head = None
            value = old_head.value
            self.length -= 1
        return value

    def remove_tail(self):
        value = None
        old_tail = self.tail
        if old_tail is not None:
            i = self.head
            j = None
            while i is not old_tail:
                j = i
                i = i.next
            if j is not None:
                j.next = None
            self.tail = j
            value = old_tail.value
            if self.head is old_tail:
                self.head = None
        return value

    def pop(self):
        self.remove_tail()
