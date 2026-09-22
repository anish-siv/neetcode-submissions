# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            # what do you need to save before you overwrite curr.next?
            next_node = curr.next
            
            # how do you reverse the current link?
            curr.next = prev
            
            # how do you move prev and curr forward?
            prev = curr             # advance
            curr = next_node        # advance            
            
        # what do you return, and why?
        return prev