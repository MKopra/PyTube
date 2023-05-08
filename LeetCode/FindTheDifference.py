# first stab at it - didn't write everything out because hubris 
# got stuck, here's my first shot at it 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        if len(count_s) == len(count_t):
            for i in range(len(t)):
                if list(count_s.values())[i] != list(count_t.values())[i]:
                    return list(count_t)[i]
        if len(count_s) != len(count_t):
            for i in range(len(s)):
                if list(count_t)[i] in count_t and list(count_t)[i] not in list(count_s)[i]:
                    return list(count_t)[i]

# asked chatGPT for help, modified my code to this 

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        if len(count_s) == len(count_t): # same length meaning that the extra char is a duplicate
            for char in count_t: 
                if count_t[char] != count_s[char]: # if the value at at character is not equal (more counts of char in one then other) then return char
                    return char
        if len(count_s) != len(count_t): # char we're looking for isn't in s at all/not duplicate
            for char in count_t:
                if count_t[char] > count_s[char]: #if the value at a key in count t is greater that count s, that's the new key 
                    return char # return the new key with the diff