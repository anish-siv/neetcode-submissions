# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        carry = 0
        while l1 or l2 or carry:
            sum_node = ListNode() # Create a node for the sum of l1 and l2
            x = l1.val if l1 else 0 # If l1 exists, get the value, else it is 0
            l1 = l1.next if l1 else None # If l1 exists, get the next value, else it is None
            y = l2.val if l2 else 0 # If l2 exists, get the value, else it is 0
            l2 = l2.next if l2 else None # If l2 exists, get the next value, else it is None
            column_total = x + y + carry
            digit = column_total % 10 # Getting the digit
            carry = column_total // 10 # Getting the carry
            sum_node.val = digit
            tail.next = sum_node
            tail = sum_node
        return dummy.next
            


        