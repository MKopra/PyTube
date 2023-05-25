class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    counter = counter + 1
            output.append(counter)
        return output
    
# worked on the first try fuck yeah