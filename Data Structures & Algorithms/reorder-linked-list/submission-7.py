# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        fast_head = slow.next
        slow.next = None   

        slow = head
        fast = fast_head

        prev = None

        while fast:
            next_node = fast.next
            fast.next = prev
            prev = fast
            fast = next_node

        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
        



            