# this is the method to recursively update the val from the biggest to smallest, from the right to left
class Solution:
    def __init__(self):
        # it is used to store the cumulative sum of the bigger values compared to the current value
        self.val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right:
            self.bstToGst(root.right)
        root.val = self.val = self.val + root.val
        if root.left:
            self.bstToGst(root.left)
        return root

# Runtime: 20 ms, faster than 99.40% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
