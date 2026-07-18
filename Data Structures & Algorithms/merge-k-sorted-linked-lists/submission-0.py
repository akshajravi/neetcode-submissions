# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            merged = []

            for i in range(1,len(lists),2):
                l1 = lists[i-1]
                l2 = lists[i]
                merged.append(mergeTwoLists(l1,l2))

            if len(lists) % 2 == 1:
                merged.append(lists[-1])
            
            lists = merged
        
        return lists[-1]
        
    




def mergeTwoLists(l1,l2):
        
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next

