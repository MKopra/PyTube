class Solution:
    def countBits(self, n: int) -> List[int]:
        numbers = [i for i in range(n+1)]
        binList = []
        result = []
        for i in range(len(numbers)):
            binary = bin(numbers[i])
            binList.append(binary)
        for i, m in enumerate(binList):
            count = 0 
            for n in m:
                if n == '1':
                    count += 1
                result.append(count)
        return result
