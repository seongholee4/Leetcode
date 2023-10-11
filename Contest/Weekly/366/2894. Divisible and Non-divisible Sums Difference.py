class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1, n+1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        
        return num1 - num2
    
s = Solution()
n = 5
m = 6
print(s.differenceOfSums(n, m))
