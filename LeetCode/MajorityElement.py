class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums = Counter(nums) # dictionary of key value pairs
        count_values = list(count_nums.values())
        count_keys = list(count_nums.keys())
        max_value = max(count_values)
        for i in range(len(count_keys)):
            if count_values[i] == max_value:
                return count_keys[i]

# squabbled with the index() function a bit, figured it out, just looped through keys