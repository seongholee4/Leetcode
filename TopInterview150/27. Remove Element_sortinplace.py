from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                count += 1
                nums[i] = 1000
            i += 1
        nums.sort()
        return len(nums) - count

            

    

s = Solution()
print(s.removeElement([3,2,2,3], 3))  # replace with your actual implementation
print(s.removeElement([0,1,2,2,3,0,4,2], 2))