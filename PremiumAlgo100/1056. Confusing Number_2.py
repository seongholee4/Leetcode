class Solution:
    def confusingNumber(self, n: int) -> bool:
        a = {0: '0', 1: 1, 2: False, 3: False, 4: False,
             5: False, 6: 9, 7: False, 8: 8, 9: 6}
        # Initialize a hashmap invertMap that converts each valid digit to its inverted digit, set rotatedNumber = 0.
        rotatedNumber = 0
        n_ = n
        # Keep getting the last digit res of n by taking the modulo of n to 10:
        while n_:
            res = n_ % 10
            # If res is not in invertMap, return false.
            if a[res] == False:
                return False
            # append res to the end of rotatedNumber 
            # by setting rotatedNumber = rotatedNumber * 10 + invertMap[res]. When we multiply rotatedNumber by 10, that is equivalent to adding a 0 to the end. 
            # Then, adding invertMap[res] will set the last digit.
            rotatedNumber = rotatedNumber * 10 + int(a[res])
            print(rotatedNumber)
            n_ //= 10
        
        if rotatedNumber == n:
            return False
        else:
            return True

s = Solution()
n = 160
res = s.confusingNumber(n)
print(res)
