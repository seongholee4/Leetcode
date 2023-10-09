from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s_ = s
        new_word = ""
        for matrix in shift:
            direction = matrix[0]
            amount = matrix[1]
            # grab letters from s by "amount"
            # if direction is 1: catch letters from the end to + amount backwards
            # if direction is 0 (left): catch letters from the beginning to + amount index
            if direction == 1:
                amount = amount % len(s_)
                catch = s_[-amount:]
                new_word = catch + s_[:-amount]
            if direction == 0:
                amount = amount % len(s_)
                catch = s_[:amount]
                new_word = s_[amount:]+ catch

            s_ = new_word
        return s_

t = Solution()
s = "abc"
# directioni can be 0 (for left shift) or 1 (for right shift).
# amounti is the amount by which string s is to be shifted.
shift = [[0,1],[1,2]]

s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]

s = "abc"
shift = [[1,4]]
print(t.stringShift(s,shift))

