from collections import defaultdict, deque

class FreqStack(object):
    def __init__(self):
        self.queue = deque #use of the main structure - queue
        self.freq = defaultdict(int)
        self.group = defaultdict(self.queue)
        self.max_f = 0 #max frequency

    def push(self, value):
        """
        :type val: int
        :rtype: None
        """
        self.group[self.freq[value] + 1].append(value)
        self.freq[value] += 1
        self.max_f = max(self.max_f, self.freq[value])


    def pop(self):
        """
        :rtype: int
        """
        value = self.group[self.max_f].pop()
        self.freq[value] -= 1

        if not self.group[self.max_f]:
            self.max_f -= 1

        return value
