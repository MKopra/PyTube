# recursive solution without defining prev pointer

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_node = self.reverseList(head.next)
        head.next.next = head              
        head.next = None
        return new_node
    
# recursive with prev pointer defined -> did this because this is how I saw an example solved and was confused by it
# looks like you just have to define another function within it and call that recursively 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, previous: ListNode = None) -> ListNode:
            if node is None:
                return previous
            next_node = node.next
            node.next = previous
            return reverse(next_node, node)
        
        return reverse(head)
    
#alright how about non recursively/iteratively

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        while head: # use a while loop to loop through the linked list "while listnode"
            next = head.next
            head.next = prev # the next is the previous
            prev = head 
            head = next
        return prev
    
