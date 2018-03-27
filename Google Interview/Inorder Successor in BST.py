"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):

        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        ret = None
        curr = root
        while curr != None:
            if p.val < curr.val:
                ret = curr
                curr = curr.left
            elif p.val >= curr.val:
                curr = curr.right

        return ret

r = TreeNode(2)
r.left = None
r.right = TreeNode(3)

mySol = Solution()
stuff = mySol.inorderSuccessor(r, r)

print 'suh'


