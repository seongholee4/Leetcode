from typing import List


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

"""
nums1 = [0]
nums2 = [1]
m = 0
n = 1
"""
""" 
nums1 = [1]
nums2 = []
m = 1
n = 0
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        _  """
        if n == 0:
            return
        if m == 0:
            nums1 = nums2.copy()
            return
        left = 0
        right = m
        p = 0

        while left < m:
            """ 
            nums1 = [1,2,6,0,0,0]
            nums2 = [2,5,6]
            nums1 = [1,2,2,6,0,0]
            nums2 = [2,5,6]
            nums1 = [1,2,2,5,6,0]
            nums2 = [2,5,6]
            nums1 = [1,2,2,5,6,0]
            nums2 = [2,5,6]
            """
            if nums1[left] <= nums2[p]:
                left += 1
            else: 
                nums1[right] = nums1[left]
                right += 1
                nums1[left] = nums2[p]
                p+=1
                left+=1
        

                



s = Solution()
print(s.merge(nums1, m, nums2, n))
# print(nums1)