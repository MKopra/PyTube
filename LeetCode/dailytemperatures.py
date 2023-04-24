from typing import List

# O(n^2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resultList = []
        for i,m in enumerate(temperatures):
            found = False 
            for j,k in enumerate(temperatures[i+1:]):
                if k > m:
                    diff = (j+1)
                    resultList.append(diff)
                    found = True
                    break
            if not found:
                resultList.append(0)
        return resultList
    
    # O(n) from Leetcode
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        
        return result


