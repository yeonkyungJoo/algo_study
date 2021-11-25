# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        return []

if __name__ == "__main__":
    head = [1,2,3,4,5]
    left = 2
    right = 4
    print(Solution().reverseBetween(head, left, right))