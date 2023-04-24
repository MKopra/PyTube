
class Solution(object):
    def romanToInt(s:str) -> int:
        I = 1
        V = 5
        X = 10 
        L = 50
        C = 100
        D = 500
        M = 1000
        counter = {}
        for letter in s:
            if letter not in counter:
                counter[letter] = 0
            counter[letter] += 1
        Icount = counter.get('I', 0)
        Vcount = counter.get('V', 0)
        Xcount = counter.get('X', 0)
        Lcount = counter.get('L', 0)
        Ccount = counter.get('C', 0)
        Dcount = counter.get('D', 0)
        Mcount = counter.get('M', 0)
        masterCount = Icount+(Vcount*V)+(Xcount*X)+(Lcount*L)+(Ccount*C)+(Dcount*D)+(Mcount*M)
        print("Roman To  Integer Value:", masterCount)
    s = input()
    romanToInt(s)