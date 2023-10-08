class Solution:
    def confusingNumber(self, n: int) -> bool:
        a = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        # Store each digit of int n to array
        s = str(n)
        # print(s)
        
        inverted_num = []
        # for each char in s, invert each digit. If not invertible, return false
        for i in range(len(s)-1, -1, -1):
            chr = s[i]
            if chr not in a:
                return False
            # store each inverted digit into an array form.
            inverted_num.append(a[chr])# appends to the end of the list
            # print(inverted_num)
        rotated_num = int("".join(inverted_num))
        if rotated_num == n:
            return False
        else:
            return True




s = Solution()
n = 160
print(s.confusingNumber(n))