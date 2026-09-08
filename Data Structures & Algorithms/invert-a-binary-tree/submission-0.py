# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertNode(node):
            if node == None:
                return 

            invertNode(node.left)
            invertNode(node.right)

            temp = node.left
            node.left = node.right
            node.right = temp
        
        invertNode(root)
        return root
