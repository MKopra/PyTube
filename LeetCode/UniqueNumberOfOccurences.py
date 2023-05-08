from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countList = []
        count = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    count +=1
                    countList.append(count)
        countLen = len(countList)
        countSet = set(countList)
        returnLen = len(countSet)
        if returnLen == countLen:
            return True
        if returnLen != countLen:
            return False
        
#accepted method 1
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countList = []
        counted = set()
        for i in range(len(arr)):
            if arr[i] not in counted:
                count = 0
                for j in range(len(arr)):
                    if arr[i] == arr[j]:
                        count +=1
                countList.append(count)
                counted.add(arr[i])
        countSet = set(countList)
        if len(countList) == len(countSet):
            return True
        else:
            return False
        
#method2 lets do it with a dict


#method 3 lets do it with a counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countDict = Counter(arr)
        return len(set(countDict.values())) == len(countDict.values())
    