class Solution:
    def romanToInt(self, s: str) -> int:        
        Roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0 
        for i in range(len(s)):
            if i + 1 < len(s) and Roman[s[i + 1]] > Roman[s[i]]:
                result -= Roman[s[i]]
            else:
                result += Roman[s[i]]
                
        return result

