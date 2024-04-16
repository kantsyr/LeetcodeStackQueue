class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_n = Node(value)

        if self.tail and self.tail is not new_n:
            self.tail.next = new_n

        self.tail = new_n

        if self.head is None:
            self.head = self.tail

    def pop(self):
        value = self.head.data

        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def is_empty(self):
        return self.head is None

class MyStack(object):
    def __init__(self):
        self.queue_1 = Queue()
        self.queue_2 = Queue()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue_2.add(x)

        while not self.queue_1.is_empty():
            self.queue_2.add(self.queue_1.pop())

        self.queue_1, self.queue_2 = self.queue_2, self.queue_1
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue_1.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue_1.head.data
   
    def empty(self):
        """
        :rtype: bool
        """
        return self.queue_1.is_empty()
