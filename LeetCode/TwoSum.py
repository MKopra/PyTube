class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif = []
        for i in range(len(nums)):
            dif.append(target - nums[i]) # nums[i] is the same thing as v syntax wise, important to note
            if (dif[i] in nums[i+1:]): # only works when sequential
                return [i, nums.index(dif[i], i+1)] # returns the indicies for when the difference is in the list, and the next number, kind of understand, kind of not
            return []

        # nums[i+1:] means a list, not nums[i+1] which is the next int in the array/list nums[]