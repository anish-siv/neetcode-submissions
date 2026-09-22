# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head # Set current pointer as head
        seen = set() # Initialize empty set to gather seen elements
        
        while curr is not None: # While curr is not empty
            if curr in seen: # If yes — we've looped back to a node we've been at before, so there's a cycle
                return True 
            else: # If it wasn't in seen, add curr to seen now, so future iterations can recognize it.
                seen.add(curr)
            curr = curr.next # Advance curr

        return False