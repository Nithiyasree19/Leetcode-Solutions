# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        memo = {}

        def build(left, right):
            if left > right:
                return [None]

            if (left, right) in memo:
                return memo[(left, right)]

            result = []

            for root_val in range(left, right + 1):
                left_trees = build(left, root_val - 1)
                right_trees = build(root_val + 1, right)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val)
                        root.left = left_tree
                        root.right = right_tree
                        result.append(root)

            memo[(left, right)] = result
            return result

        return build(1, n)      