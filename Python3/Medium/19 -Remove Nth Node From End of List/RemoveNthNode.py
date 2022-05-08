# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# First Try
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        
        for i in range(n):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        
        tmp1, tmp2 = left.next, left.next.next
        tmp1.next = None
        left.next = tmp2
        return dummy.next

# Concise Solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        
        for i in range(n):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
