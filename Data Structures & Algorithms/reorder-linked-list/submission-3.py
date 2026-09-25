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
            slow = slow.next # Move slow by 1
            fast = fast.next.next # Move fast by 2

        second = slow.next
        slow.next = None
        first = head

        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        while first and prev:
            tmp1 = first.next
            tmp2 = prev.next

            first.next = prev
            prev.next = tmp1

            first = tmp1
            prev = tmp2
        return prev



