class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        if len(numSet) == len(nums):
            return False 
        if len(numSet) != len(nums):
            return True 