# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [] # result = []
        if not root: # if the tree is empty: return what?
            return result
        q = deque([root]) # q = deque([root])
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val) # record node.val in level
                if node.left: q.append(node.left) # add it to the queue
                if node.right: q.append(node.right) # add it to the queue
            result.append(level) # add level to result
        return result