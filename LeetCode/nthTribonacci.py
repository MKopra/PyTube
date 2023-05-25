
# tried recursively first and didnt work
class Solution:
    def tribonacci(self, n: int) -> int:
        F = [0]*38
        for i in range(0,38):
            F[0] = 0
            F[1] = 1
            F[2] = 1
            F[i+3] = F[i] + F[i+1] + F[i+2]
            F.append(F[i])
        print(F)
        return F[n]

Solution.tribonacci(Solution, 20)