# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root:
            arr = []
            self.inOrder(root,arr)
        return arr[k-1]
        
        
    def inOrder(self, root, arr):

        if root:
            self.inOrder(root.left,arr)
            arr.append(root.val)
            self.inOrder(root.right,arr)

