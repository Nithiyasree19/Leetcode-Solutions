# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        prev = None
        current = root

        while current:
            if not current.left:
                if prev and prev.val > current.val:
                    if first is None:
                        first = prev
                    second = current

                prev = current
                current = current.right

            else:
                predecessor = current.left

                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None

                    if prev and prev.val > current.val:
                        if first is None:
                            first = prev
                        second = current

                    prev = current
                    current = current.right

        first.val, second.val = second.val, first.val        