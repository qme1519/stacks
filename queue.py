class LinearQ:
    def __init__(self, size):
        self.size = size
        self.q = [None] * size
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if not self.isFull():
            self.q[self.tail] = value
            self.tail += 1
        else:
            return False
    def dequeue(self):
        if not self.isEmpty():
            temp = self.q[self.head]
            self.head += 1
            return temp
        else:
            return False
    def isEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False
    def isFull(self):
        if self.tail == self.size:
            return True
        else:
            return False
        
class CircularQ:
    def __init__(self, size):
        self.size = size
        self.q = [None] * size
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if not self.isFull():
            self.q[self.tail] = value
            self.tail += 1
        else:
            return False
    def dequeue(self):
        if not self.isEmpty():
            temp = self.q[self.head]
            self.head += 1
            return temp
        else:
            return False
    def isEmpty(self):
        if self.head == self.tail:
            return True
        else:
            if self.head == self.size:
                self.head = 0
            return False
    def isFull(self):
        if self.tail == self.size:
            if self.head != 0:
                self.tail=0
                return False
            else:
                return True
        elif self.tail == self.head and self.head != 0:
            return True
        else:
            return False
        
