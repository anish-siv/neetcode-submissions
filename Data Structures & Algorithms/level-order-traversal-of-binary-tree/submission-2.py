# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root is None:
            return result

        q = deque([root])
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(level)
        return result
        # Create a empty list result

        # Create base case
        # If root is None
            # Return result
        # Create a deque q that starts with root
        # While q
            # Create a variable level_size that is the length of q
            # Create empty list level_size
            # For _ in range level_size
                # Create a node variable that pops the left of q (q.popleft())
                # If node.left: level.append(node.left)
                # If node.right: level.append(node.right)
                # Append list level to result
        # Return result
