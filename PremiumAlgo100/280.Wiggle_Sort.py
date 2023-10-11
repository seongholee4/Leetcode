from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums)-1, 2):
            self.swap(nums, i, i+1)
        
    def swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]
        
    
s = Solution()
nums = [3,5,2,1,6,4]
s.wiggleSort(nums)
        