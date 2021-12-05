class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()
    def peek(self) -> int:
        while not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []

if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    print(q.peek())
    print(q.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()