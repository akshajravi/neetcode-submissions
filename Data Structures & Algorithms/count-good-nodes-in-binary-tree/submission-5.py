# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,maxVal):
            if not node:
                return 0

            #we add one to the count of good nodes if its greater than or equal to the max of the nodes before it 
            res = 1 if node.val >= maxVal else 0

            maxVal = max(maxVal,node.val)
            res += dfs(node.left,maxVal)
            res += dfs(node.right,maxVal)

            return res 

        return dfs(root,root.val)



