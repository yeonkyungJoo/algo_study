class ListNode:
    def __init__(self, value, prev = None, next = None):
        self.val = value
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        # k는 deque의 정해진 크기이다.
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
    # # 작동하지 않음 ㅠㅠ
    # def print_all(self):
    #     ptr = self.head
    #     while ptr is not None:
    #         print(ptr.val, end=" ")
    #         ptr = ptr.next
    #     print()

    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


if __name__ == '__main__':
    myCircularDeque = MyCircularDeque(3);
    print(myCircularDeque.insertLast(1));  #// return True
    print(myCircularDeque.insertLast(2));  #// return True
    print(myCircularDeque.insertFront(3)); #// return True
    print(myCircularDeque.insertFront(4)); #// return False, the queue is full.
    print(myCircularDeque.getRear());      #// return 2
    print(myCircularDeque.isFull());       #// return True
    print(myCircularDeque.deleteLast());   #// return True
    print(myCircularDeque.insertFront(4)); #// return True
    print(myCircularDeque.getFront());     #// return 4
    myCircularDeque.print_all()