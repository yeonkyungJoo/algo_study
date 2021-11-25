# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return False

if __name__ == "__main__":
    head = [1,2,2,1]
    print(Solution().isPalindrome(head))