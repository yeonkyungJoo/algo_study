from typing import List
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next

if __name__ == '__main__':
    solution = Solution()
    list1_3 = ListNode(4, None)
    list1_2 = ListNode(4, list1_3)
    list1 = ListNode(1, list1_2)
    list2_3 = ListNode(4, None)
    list2_2 = ListNode(3, list2_3)
    list2 = ListNode(1, list2_2)
    list3_2 = ListNode(6, None)
    list3 = ListNode(2, list3_2)
    lists = [list1, list2, list3]
    print(solution.mergeKLists(lists))
