# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return 
        
        #Find the middle node

        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half of the list
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head2 = prev

        while head2:
            temp1,temp2 = head.next, head2.next
            head.next = head2
            head2.next = temp1
            head,head2 = temp1 , temp2 


