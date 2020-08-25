from linkedlist import LinkedList, Node

ll = LinkedList()
print("Empty LinkedList")
print("Expected: []")
print(ll) # []

print("\nAdd to Tail")
print(f"Append 1: {ll.append(1)}")
print(f"Push 42: {ll.push(42)}")
print(f"Add_To_Tail 98: {ll.add_to_tail(98)}")
new_node = Node(9)
print(f"Add_Node_To_Tail 9: {ll.add_node_to_tail(new_node)}")
print("Expected: [1, 42, 98, 9]")
print(ll) # [1, 42, 98, 9]

print("\nAdd to Head")
print(f"Unshift 56: {ll.unshift(56)}")
print(f"Add_To_Head 13: {ll.add_to_head(13)}")
print(f"Unshift 72: {ll.unshift(72)}")
another_node = Node(22)
print(f"Add_Node_to_Head 22: {ll.add_node_to_head(another_node)}")
print("Expected: [22, 72, 13, 56, 1, 42, 98, 9]")
print(ll) # [22, 72, 13, 56, 1, 42, 98, 9]

print("\nRemove from Head")
print(f"Shift: {ll.shift()}")
print(f"Remove_Head: {ll.remove_head()}")
print("Expected: [13, 56, 1, 42, 98, 9]")
print(ll) # [13, 56, 1, 42, 98, 9]

print("\nRemove from Tail")
print(f"Pop: {ll.pop()}")
print(f"Remove_tail: {ll.remove_tail()}")
print("Expected: [13, 56, 1, 42]")
print(ll) # [13, 56, 1, 42]

print("\nRemove by Index")
print(f"Remove_at_index(2): {ll.remove_at_index(2)}")
print("Expected: [13, 56, 42]")
print(ll) # [13, 56, 42]
