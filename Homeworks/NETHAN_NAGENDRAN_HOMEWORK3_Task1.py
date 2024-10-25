class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def remove(self, node):
        if self.head == self.head.next:  # Only one node
            self.head = None
        else:
            current = self.head
            while current.next != node:
                current = current.next
            current.next = node.next
            if node == self.head:
                self.head = node.next

def one_potato_two_potato(n, k):
    # Create a circular linked list with group_size nodes
    circle = CircularLinkedList()
    for i in range(n):
        circle.append(i)

    current = circle.head
    while circle.head != circle.head.next:  # More than one node in the list
        # Move steps-1 steps
        for _ in range(k - 1):
            current = current.next
        # Remove the steps-th node
        circle.remove(current)
        current = current.next

    return circle.head.value

group_size = 11  
steps = 8       
print(one_potato_two_potato(group_size, steps))  # Output: 8
