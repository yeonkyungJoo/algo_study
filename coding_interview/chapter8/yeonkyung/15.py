# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return None

if __name__ == "__main__":
    head = [1,2,3,4,5]
    print(Solution().reverseList(head))