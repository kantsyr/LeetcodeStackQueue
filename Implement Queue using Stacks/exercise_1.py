class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyQueue(object):
    def __init__(self):
        self.stack = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.stack is None:
            self.stack = Node(x)
        else:
            new_n = Node(x)
            new_n.next = self.stack
            self.stack = new_n

    def pop(self):
        """
        :rtype: int
        """
        current = self.stack
        previous = None

        while current.next is not None:
            previous = current
            current = current.next

        if previous is not None:
            previous.next = None
        else:
            self.stack = None

        return current.value

    def peek(self):
        """
        :rtype: int
        """
        current = self.stack

        while current.next is not None:
            current = current.next

        return current.value

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack
