from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        reader = 0
        writer = 0
        while reader < len(nums):
            if nums[reader] == val:
                reader += 1
            elif nums[reader] != val:
                nums[writer] = nums[reader]
                reader += 1
                writer += 1
            print(nums)
            if reader != len(nums):
                print("reader:", reader, nums[reader])
            print("writer:", writer, nums[writer])

        return writer

            

    

s = Solution()
print(s.removeElement([3,2,2,3], 3))  # replace with your actual implementation
print(s.removeElement([0,1,2,2,3,0,4,2], 2))