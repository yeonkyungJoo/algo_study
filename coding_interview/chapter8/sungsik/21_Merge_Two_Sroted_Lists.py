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
# class Solution:
#     def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
#         if (not list1) or (list2 and list1.val > list2.val):
#             list1, list2 = list2, list1
#         if list1:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#         return list1
#
#
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

if __name__ == '__main__':
    list1_3 = ListNode(4, None)
    list1_2 = ListNode(2, list1_3)
    list1 = ListNode(1, list1_2)
    list2_3 = ListNode(3, None)
    list2_2 = ListNode(2, list2_3)
    list2 = ListNode(1, list2_2)
    result = Solution().mergeTwoLists(list1, list2)
    result.print_all()
