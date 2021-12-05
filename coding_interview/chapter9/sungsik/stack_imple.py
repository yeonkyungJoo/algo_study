class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

    def _print_all(self):
        while self:
            print(self.val, end=' ')
            self = self.next
        print()

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

if __name__ == '__main__':
    s = Stack()
    for i in range(5):
        s.push(i)
    print(s.pop())
    print(s.pop())
    print(s.pop())
