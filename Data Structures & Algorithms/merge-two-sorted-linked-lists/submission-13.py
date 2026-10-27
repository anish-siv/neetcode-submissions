# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy ListNode
        # Create a l1 ListNode (Start at list1)
        # Create a l2 ListNode (Start at list2)

        # Compare the first values of both linked lists
        # If the values on both lists are equal, start with list1 (dummy's next will point at l1)
        # Increment l1 pointer by 1
        # Compare 
        
        
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val: # If list1 value is <= list2 value
                tail.next = list1 # Set the tail to point to list1
                list1 = list1.next # Move list1 ahead by 1
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        
        tail.next = list1 or list2

        return dummy.next

                

        