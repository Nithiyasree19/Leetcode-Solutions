# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.answer = float("-inf")

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Path passing through this node
            self.answer = max(self.answer, node.val + left + right)

            # Best path extending upward to the parent
            return node.val + max(left, right)

        dfs(root)
        return self.answer