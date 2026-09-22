# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next






# def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
#     # 1. Create a dummy node to act as the head of the new list
#     dummy = ListNode()
#     current = dummy
    
#     # 2. Loop until one of the lists becomes empty
#     while l1 and l2:
#         if l1.val <= l2.val:
#             current.next = l1
#             l1 = l1.next  # Move l1 pointer forward
#         else:
#             current.next = l2
#             l2 = l2.next  # Move l2 pointer forward
#         current = current.next  # Move the combined list pointer forward
        
#     # 3. Append the remaining elements of the non-empty list
#     current.next = l1 if l1 else l2
    
#     # Return the actual head (skipping the dummy node)
#     return dummy.next
