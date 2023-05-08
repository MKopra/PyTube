# first shot at it
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:  # Check if head is None
            return False
        else:
            return True
        return self.hasCycle(head)
    
# I will say my algo as correct my implementation just sucked

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        def helper(current, visited):
            if not current:
                return False

            if current in visited:
                return True

            visited.add(current)

            return helper(current.next, visited)


        return helper(head, set())