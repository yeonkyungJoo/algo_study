class MyQueue:

    def __init__(self):
        self.s1 = []    # append
        self.s2 = []    # pop

    def push(self, x: int) -> None:
        while self.s2:
            _x = self.s2.pop()
            self.s1.append(_x)
        self.s1.append(x)

    def pop(self) -> int:
        while self.s1:
            _x = self.s1.pop()
            self.s2.append(_x)
        return self.s2.pop()

    def peek(self) -> int:
        while self.s1:
            _x = self.s1.pop()
            self.s2.append(_x)
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()