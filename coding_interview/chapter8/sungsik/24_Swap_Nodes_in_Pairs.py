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
    # 값만 교환
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

    # 반복 구조로 스왑
    def swapPairs2(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next

        return root.next

    # 재귀 구조로 스왑
    def swapPairs3(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs3(p.next)
            p.next = head
            return p
        return head

if __name__ == '__main__':
    list4 = ListNode(4, None)
    list3 = ListNode(3, list4)
    list2 = ListNode(2, list3)
    list = ListNode(1, list2)

    # result = Solution().swapPairs(list)
    # result._print_all()

    # result2 = Solution().swapPairs2(list)
    # result2._print_all()

    result3 = Solution().swapPairs3(list)
    result3._print_all()
