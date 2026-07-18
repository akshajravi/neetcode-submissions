# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        
        for i in range(n+1):
            if second == None:
                return head.next
            second = second.next
        
        
        #now we need to go to end with two pointer approach
        while second:
            first = first.next
            second = second.next

        first.next = first.next.next

        return head