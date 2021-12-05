class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.h_ptr = 0
        self.t_ptr = 0
    def enQueue(self, value: int) -> bool:
        if self.q[self.t_ptr] is None:
            self.q[self.t_ptr] = value
            self.t_ptr = (self.t_ptr + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.h_ptr] is None:
            return False
        else:
            self.q[self.h_ptr] = None
            self.h_ptr = (self.h_ptr + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.h_ptr] is None else self.q[self.h_ptr]

    def Rear(self) -> int:
        return -1 if self.q[self.t_ptr - 1] is None else self.q[self.t_ptr - 1]

    def isEmpty(self) -> bool:
        return self.h_ptr == self.t_ptr and self.q[self.h_ptr] is None

    def isFull(self) -> bool:
        return self.h_ptr == self.t_ptr and self.q[self.h_ptr] is not None


if __name__ == '__main__':
    cq = MyCircularQueue(5)
    print(cq.isEmpty())
    print(cq.isFull())
    print(cq.Front())
    print(cq.Rear())
    print(cq.deQueue())
    print(cq.enQueue(1))
    print(cq.Front())
    print(cq.Rear())
    print(cq.enQueue(2))
    print(cq.Front())
    print(cq.Rear())
    print(cq.enQueue(3))
    print(cq.enQueue(4))
    print(cq.Front())
    print(cq.Rear())
    print(cq.deQueue())
    print(cq.Front())
    print(cq.Rear())
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()