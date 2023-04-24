# method 1: slowpoke method (accidentally misread prob, this returns a new list, should alter list)

#method 2: dummy list then equal
''' FIRST TRY
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        resultList = []
        for i,m in enumerate(nums[i]):
            if nums[0] < nums[1]:
                resultList.append(nums[0])
            if nums[1] < nums[0]:
                resultList.append(nums[1])
            if i % 1 != 0:
                if nums[i] < (resultList[i-1]):
                    resultList.append(nums[i])
            if i % 1 == 0: 
                if nums[i] > (resultList[i-1]):
                    resultList.append(nums[i])
        nums[:] = resultList'''
'''SECOND TRY with help
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        resultList = []
        for i in range(len(nums)):
            if i != 0 and i % 2 == 1 and nums[i] > resultList[i-1]:
                resultList.append(nums[i])
            elif i != 0 and i % 2 == 0 and nums[i] < resultList[i-1]:
                resultList.append(nums[i])
            else:
                resultList.append(nums[i])
        nums[:] = resultList
        
        returns the wrong values in nums[], actual solution uses in-place swapping'''
#metod 3: what was the real answer in O(n)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i % 2 == 1 and nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            elif i % 2 == 0 and nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]

        # only passed 28/52 cases

        # REAL ANSWER

        class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Sort the input array
        nums.sort()
        
        # Split the sorted array into two halves
        n = len(nums)
        mid = n // 2
        first_half = nums[:mid]
        second_half = nums[mid:]
        
        # Interleave the elements of the two halves
        result = []
        for i in range(mid):
            result.append(first_half[i])
            result.append(second_half[i])
        if n % 2 != 0:
            result.append(first_half[-1])
        
        # Copy the result back to the input array
        for i in range(n):
            nums[i] = result[i]