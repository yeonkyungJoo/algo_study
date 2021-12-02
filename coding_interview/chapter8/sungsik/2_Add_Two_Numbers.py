from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def _print_all(self):
        while self:
            print(self.val, end= ' ')
            self = self.next
        print()


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def SLL_to_List(self, node:ListNode) -> List:
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def list_to_SLL(self, list: str) -> ListNode:
        prev: ListNode = None
        for r in list:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.SLL_to_List(self.reverseList(l1))
        b = self.SLL_to_List(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        return self.list_to_SLL(str(resultStr))


    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next


if __name__ == '__main__':
    list1_3 = ListNode(3, None)
    list1_2 = ListNode(4, list1_3)
    list1 = ListNode(2, list1_2)
    list2_3 = ListNode(4, None)
    list2_2 = ListNode(6, list2_3)
    list2 = ListNode(5, list2_2)

    # result = Solution().addTwoNumbers(list1, list2)
    # result._print_all()
    result2 = Solution().addTwoNumbers2(list1, list2)
    result2._print_all()