"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        node = ListNode(value)
        return self.add_node_to_head(node)

    def add_node_to_head(self, node): # separate fn b/c it makes moving easier
        if self.head is None: # list is empty, so becomes list of 1
            self.head = node
            self.tail = node
        else: # general case
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1
        return self.length

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length <= 0: # list is empty
            return None
        elif self.length == 1: # if list has 1 node, remove it and clear the list
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else: # general case
            value = self.head.value
            new_head = self.head.next
            new_head.prev = None
            self.head.next = None
            self.head = new_head
            self.length -= 1
            return value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        node = ListNode(value)
        return self.add_node_to_tail(node)

    def add_node_to_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return self.length

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length <= 0:
            return None
        elif self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.tail.value
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail.prev = None
            self.tail = new_tail
            self.length -= 1
            return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_node_to_head(node) # this is where the separate fn saves us some repetition

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_node_to_tail(node)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None: # empty list
            return None
        if self.length == 1: # single node
            if self.head is node:
                value = self.head.value
                self.head = None
                self.tail = None
                self.length = 0
                return value
            else:
                return None
        # current_node = self.head
        # for _ in range(self.length): # gotta check all the nodes
        #     if current_node is node:
        #         break
        #     else:
        #         current_node = current_node.next
        if node.prev is not None:
            node.prev.next = node.next
            if node is self.tail:
                self.tail = node.prev
        if node.next is not None:
            node.next.prev = node.prev
            if node is self.head:
                self.head = node.next
        node.prev = None
        node.next = None
        self.length -= 1
        return node.value
        # previous = current_node.prev
        # next = current_node.next
        # value = current_node.value
        # if previous is not None:
        #     previous.next = next
        #     if current_node is self.tail:
        #         self.tail = previous
        # if next is not None:
        #     next.prev = previous
        #     if current_node is self.head:
        #         self.head = next
        # current_node.next = None
        # current_node.prev = None
        # self.length -= 1
        # return value

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        current_max = self.head.value
        current_node = self.head
        for i in range(self.length):
            if current_node.value > current_max:
                current_max = current_node.value
            current_node = current_node.next
        return current_max
