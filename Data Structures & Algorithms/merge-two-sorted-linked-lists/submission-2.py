# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2: # While list1 and list2 are being iterated upon
            if list1.val <= list2.val: # If list1 value is <= to list2 value
                curr.next = list1 # Set dummy next value to list1
                list1 = list1.next # Advance list1 pointer
            else:
                curr.next = list2 # Set dummy next value to list2
                list2 = list2.next # Advance list2 pointer
            curr = curr.next
        
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next