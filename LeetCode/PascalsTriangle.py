# here's how far I got without looking for a hint, was stumped from the start but was able to grind out this much 
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        resultLists = []
        for i in range(numRows):
            newlist = []
            if numRows == 1:
                newlist = [1]
            if numRows == 2:
                newlist = [1,1]
            else:
                for j in len(resultLists[-1])+1:
                    newlist = resultLists[-1]
            resultLists.append(newList)

# got here from a hint but got stuck again
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        resultLists = []
        for i in range(numRows):
            newlist = []
            if numRows == 1:
                newlist = [1]
            if numRows == 2:
                newlist = [1,1]
            else:
                newlist[0] = 1
                newlist[len(resultLists[-1])+1] = 1 
                for j in len(resultLists[-1])+1:
                    newlist[j] = resultLists[-1][j]+resultLists[-1][j+1]
            resultLists.append(newList)

# asked chat GPT and got this 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        resultLists = []
        for i in range(numRows):
            newlist = []
            for j in range(i+1):
                if j == 0 or j == i:
                    newlist.append(1)
                else:
                    newlist.append(resultLists[i-1][j-1] + resultLists[i-1][j])
            resultLists.append(newlist)
        return resultLists