import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = collections.deque()

        if not head:
            return True

        node = head
        while node != None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
    print(Solution().isPalindrome(head))