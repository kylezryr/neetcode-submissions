# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def visitNode(node, result):
            if node == None:
                return

            if node.left != None:
                visitNode(node.left, result)

            if node.right != None:
                visitNode(node.right, result)

            result.append(node.val)
            
            return

        result = []
        visitNode(root, result)

        return result