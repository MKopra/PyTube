import itertools

def count_combinations(n):
    numbers = [1,2]
    count = 0
    for i in range(1, len(numbers)+1):
        for combination in itertools.combinations(numbers, i):
            if sum(combination) == n:
                count += 1
    return count

# didnt work and I didnt understand it ^^

# here's neetcode's solution 

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two 
            two = temp
        return one 
    
# still not super sure, need to read alex's article all the way through and do Leetcode 509

# recursive solution 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        
        return self.climbStairs(n-1)+self.climbStairs(n-2)
        