# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# recursive solution
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        head.next = self.removeElements(head.next,val)
        return head.next if head.val == val else head
    
# iterative solution
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else:
                    curr = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head
             

#note this needs the curr dummy variable and won't function without it
