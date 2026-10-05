# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []

        queue = deque([root])

        while queue:
            curr_level = len(queue)

            for _ in range(curr_level - 1):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            # at this point, we will need to process one more element from curr_level, which is going to be right most node

            last = queue.popleft()
            res.append(last.val)
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)

        return res