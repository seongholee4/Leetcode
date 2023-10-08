class Solution:
    def confusingNumber(self, n: int) -> bool:
        a = {0: '0', 1: 1, 2: False, 3: False, 4: False, 5: False, 6: 9, 7: False, 8: 8, 9: 6}
        # n = 6
        # Store each digit of int n to array
        k = list(map(int, str(n)))
        # convert each digit and store it into a stack first in last out
        # when converting, if found false as value return false right away
        s = []
        
        for i in range(len(k)):
            temp = k[i]
            if a[temp] == False:
                return False
            else:
                s.insert(0, a[temp])
        
        converted_num = int(''.join(map(str, s)))
        if n == converted_num:
            return False
        else:
            return True
    