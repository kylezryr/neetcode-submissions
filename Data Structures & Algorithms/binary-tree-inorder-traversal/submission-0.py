# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def visitNode(node, result):
            if node == None:
                return

            if node.left != None:
                visitNode(node.left, result)

            result.append(node.val)

            if node.right != None:
                visitNode(node.right, result)
            
            return

        result = []
        visitNode(root, result)

        return result