# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
    
        # create a pointer to the dummy node
        current = dummy
        
        # iterate over both lists and compare their values
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # add the remaining nodes from the non-empty list
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # return the merged list starting from the first node after the dummy node
        return dummy.next
    
    # original try didn't work, didnt understand data structure usage, listnode not list