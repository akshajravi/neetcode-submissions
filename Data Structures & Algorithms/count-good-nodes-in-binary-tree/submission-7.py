# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_number):
            if not node:
                return 0
            curr_count = 1 if node.val >= max_number else 0
            new_max = max(max_number, node.val)

            left_count = dfs(node.left, new_max)
            right_count = dfs(node.right, new_max)
            
            return curr_count + left_count + right_count

        return dfs(root, root.val)
