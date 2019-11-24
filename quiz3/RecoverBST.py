# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = TreeNode(None)
        first = TreeNode(None)
        second = TreeNode(None)
        while (root is not None):
            if root.left is None:
                if pre.val is not None and pre.val > root.val:
                    if first.val is None:
                        first = pre
                        second = root
                    else:
                        second = root
                pre = root
                root = root.right
                # print(root.data)
                # root = root.right
            else:
                # Find the inorder predecessor of root
                temp = root.left
                while (temp.right is not None and temp.right != root):
                    temp = temp.right

                # Make root as right child of its inorder predecessor
                if (temp.right is None):
                    temp.right = root
                    root = root.left

                # Revert the changes made in if part to restore the
                # original tree i.e., fix the right child of predecessor
                else:
                    if pre is not None and pre.val > root.val:
                        if first.val is None:
                            first = pre
                            second = root
                        else:
                            second = root
                        pre = root
                    temp.right = None
                    # print(root.data)
                    root = root.right
        # swap
        if first.val is not None and second.val is not None:
            t = first.val
            first.val = second.val
            second.val = t