# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1

            while list1.next and list2:
                if list1.next.val >= list2.val:
                    tmp = list1.next
                    list1.next = list2
                    list2 = tmp

                    list1 = list1.next
                else:
                    list1 = list1.next
            if list2:
                list1.next = list2

            return head

        else:
            head = list2

            while list2.next and list1:
                if list2.next.val >= list1.val:
                    tmp = list2.next
                    list2.next = list1
                    list1 = tmp

                    list2 = list2.next
                else:
                    list2 = list2.next
            if list1:
                list2.next = list1

            return head
