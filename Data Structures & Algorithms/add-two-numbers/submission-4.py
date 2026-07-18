# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow = 0
        dummy = ListNode()
        cur3 = dummy
        while l1 and l2:

            total = l1.val + l2.val + overflow
            cur3.next = ListNode(total%10)
            overflow = total // 10
            l1 = l1.next
            l2 = l2.next
            cur3 = cur3.next

        while l1:
            total = l1.val + overflow
            cur3.next = ListNode(total%10)
            overflow = total // 10
            l1 = l1.next
            cur3 = cur3.next

        while l2:
            total = l2.val + overflow
            cur3.next = ListNode(total%10)
            overflow = total // 10
            l2 = l2.next
            cur3 = cur3.next

        if overflow:
            cur3.next = ListNode(overflow)
        return dummy.next

            
