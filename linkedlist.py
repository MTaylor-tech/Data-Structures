class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        value = "["
        pointer = self.head
        for i in range(0,self.length-1):
            value += f"{pointer.value}, "
            pointer = pointer.next
        if pointer is not None and pointer is not self.head:
            value += f"{pointer.value}"
        value += "]"
        return value

    def append(self, value):
        return self.add_to_tail(value)

    def push(self, value):
        return self.add_to_tail(value)

    def add_to_tail(self, value):
        new_node = Node(value)
        return self.add_node_to_tail(new_node)

    def add_node_to_tail(self, node):
        if self.tail is not None:
            self.tail.next = node
            self.length += 1
        else:
            self.add_node_to_head(node)
        self.tail = node
        return self.length

    def unshift(self, value):
        return self.add_to_head(value)

    def add_node_to_head(self, node):
        if self.head is not None:
            node.next = self.head
        self.head = node
        self.length += 1
        return self.length

    def add_to_head(self, value):
        new_node = Node(value)
        return self.add_node_to_head(new_node)

    def shift(self):
        return self.remove_head()

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
            self.length -= 1
            if self.head is old_tail:
                self.head = None
        return value

    def pop(self):
        return self.remove_tail()

    def remove_at_index(self, index):
        if self.length > index:
            node = self.head
            for i in range(index-1):
                node = node.next
            to_remove = node.next
            value = to_remove.value
            node.next = to_remove.next
            to_remove.next = None
            self.length -= 1
            return value
        else:
            return None
