class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        node = Node(value)
        self.size += 1

        node.next = self.head
        self.head = node

    def pop(self):
        self.size -= 1
        deleted = self.head
        self.head = self.head.next

        return deleted.data
    
    def peek(self):
        return self.head.data
    
class MyQueue(object):
    def __init__(self):
        self.queue = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.push(x)

    def pop(self):
        """
        :rtype: int
        """
        new_q_1 = Stack()
        new_q_2 = Stack()

        while not self.queue.isEmpty():
            new_q_1.push(self.queue.pop())

        result = new_q_1.pop()

        while not new_q_1.isEmpty():
            new_q_2.push(new_q_1.pop())

        self.queue = new_q_2

        return result


    def peek(self):
        """
        :rtype: int
        """
        new_q_1 = Stack()
        new_q_2 = Stack()

        while not self.queue.isEmpty():
            new_q_1.push(self.queue.pop())

        result = new_q_1.peek()

        while not new_q_1.isEmpty():
            new_q_2.push(new_q_1.pop())

        self.queue = new_q_2

        return result

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue.isEmpty()
