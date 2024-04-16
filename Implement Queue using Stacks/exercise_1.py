class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue(object):
    def __init__(self):
        self.head = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.head is None:
            self.head = Node(x)
        else:
            new_n = Node(x)
            new_n.next = self.head
            self.head = new_n

    def pop(self):
        """
        :rtype: int
        """
        current = self.head
        previous = None

        while current.next is not None:
            previous = current
            current = current.next

        if previous is not None:
            previous.next = None
        else:
            self.head = None

        return current.data

    def peek(self):
        """
        :rtype: int
        """
        current = self.head

        while current.next is not None:
            current = current.next

        return current.data

    def empty(self):
        """
        :rtype: bool
        """
        return self.head is None
