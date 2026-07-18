# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first pass - need to split list into 2 halves and reverse the second half
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        second  = slow.next
        slow.next = None
        #slow pointer is the head of second half, going to reverse now
        prev,curr = None, second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #now prev will hold head of reversed list

        head2 = prev

        while head and head2:
            temp1 = head.next
            head.next = head2
            temp2 = head2.next
            head2.next = temp1
            head = temp1
            head2 = temp2

        

