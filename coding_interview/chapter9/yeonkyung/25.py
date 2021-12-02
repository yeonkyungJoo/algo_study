# TODO - re-try
class MyCircularQueue:

    def __init__(self, k: int):
        self.list = [None] * k
        self.front = 0
        self.rear = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.list[self.rear] is None:
            self.list[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            return True
        return False

    def deQueue(self) -> bool:
        if self.list[self.front] is None:
            return False
        self.list[self.front] = None
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        return -1 if self.list[self.front] is None else self.list[self.front]

    def Rear(self) -> int:
        return -1 if self.list[self.rear - 1] is None else self.list[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.list[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.list[self.front] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()