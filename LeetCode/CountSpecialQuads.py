'''first try:
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        result = 0
        lesserNum = []
        for i,m in enumerate(nums):
            for j,k in enumerate(nums):
                if m < k:
                    lesserNum.append(m)
                    if len(lesserNum) > 2 and sum(lesserNum) < nums[i]:
                        result += 1
        return result'''
# what worked
##class Solution:
  ##  def countQuadruplets(self, nums: List[int]) -> int:
nums = [1,2,3,6]
result = 0
for i,m in enumerate(nums):
    for j,k in enumerate(nums[i+1:]):
        for l,n in enumerate(nums[j+1:]):
            for q,r in enumerate(nums[l+1:]):
                    if m <= k <= n < r and m + k + n < r:
                        result += 1
print(result)
                #return result

##accepted version
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            result += 1
        return result
    



