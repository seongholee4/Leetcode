from typing import List

class Solution:
    """
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    """
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        candidate = None
        for n in nums:
            if cnt == 0:
                candidate = n
            if candidate == n:
                cnt += 1
            else:
                cnt -= 1
        return candidate

    

s = Solution()
nums = [3,3,4]
print(s.majorityElement(nums))
