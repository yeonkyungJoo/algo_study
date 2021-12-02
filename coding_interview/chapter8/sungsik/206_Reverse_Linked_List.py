# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all(self):
        while self:
            print(self.val, end=' ')
            self = self.next
        print()
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

if __name__ == '__main__':
    list5 = ListNode(5, None)
    list4 = ListNode(4, list5)
    list3 = ListNode(3, list4)
    list2 = ListNode(2, list3)
    list = ListNode(1, list2)

    result = Solution().reverseList(list)
    result.print_all()