# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #varaible that keeps track of max path sum with split
        result = [root.val]
        
        
        #create helper functio that returns max sum without split
        
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            #if either is less than 0, ignore by setting to 0
            leftMax = max(leftMax,0)
            rightMax = max(rightMax,0)

            #keep track of max with split
            result[0] = max(result[0],root.val + leftMax + rightMax)

            #however, return max WITHOUT split

            return root.val + max(leftMax,rightMax)
        dfs(root)
        return result[0] 