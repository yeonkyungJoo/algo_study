# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        return []

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    print(Solution().mergeTwoLists(list1, list2))