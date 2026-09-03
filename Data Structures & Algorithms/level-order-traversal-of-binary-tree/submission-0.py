# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        result = []

        queue.append(root)

        while queue:
            qLen = len(queue)
            currentLevel = []
            for i in range (qLen):
                node = queue.popleft()
                if node:
                    currentLevel.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if currentLevel:
                result.append(currentLevel)

        return result