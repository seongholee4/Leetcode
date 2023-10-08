import collections
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

    
class BruteForce:
    """
    Intuition:
        We can exhaust the search space in quadratic time by checking whether each
    element is the majority element.
    
    Algorithm:
        The brute force algorithm iterates over the array, and then iterates again
    for each number to count its occurrences. As soon as a number is found to
    have appeared more than any other can possibly have appeared, return it.
    """
    def majorityElement(self, nums: List[int]) -> int:
        stop = len(nums)//2
        for num in nums:
            count = 0
            for i in nums:
                if i == num:
                    count += 1
                if count > stop:
                    return num
        return None


class HashMap:
    """
    Intuition:
        We know that the majority element occurs more than ⌊n / 2⌋ times,
        and a HashMap allows us to count element occurrences efficiently.
    
    Algorithm:
        We can use a HashMap that maps elements to counts in order to count
    occurrences in linear time by looping over nums. Then, we simply return the
    key with maximum value.
    2: 1 3: 2
    """
    def majorityElement(self, nums: List[int]) -> int:
        count = dict()
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                update = {i : 1}
                count.update(update)
        # print(count)
        stop = len(nums)//2
        for i in count:
            if count[i] > stop:
                return i
            
    def collec(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        print(counts)
        print(max(counts.keys(), key=counts.get))

class Sorting:
    """
    Intuition:
        If the elements are sorted in monotonically increasing (or decreasing) order,
    the majority element can be found at index ⌊n / 2⌋ (and also at ⌊n / 2⌋ - 1, if n is even).

    Algorithm:
        For this algorithm, we simply do exactly what is described: sort nums, and
    return the element in question. To see why this will always return the
    majority element (given that the array has one), consider the figure below
    (the top example is for an odd-length array and the bottom is for an even-length array):
    """
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

class BitManipulation:
    """
    Intuition:
        If an element majority_element occurs more than ⌊n / 2⌋ times, then there are at least ⌊n / 2⌋ elements of identical values
    with num at each bit. That is, we can reconstruct the exact value of num by combining the most frequent value (0 or 1) at each bit.

    Algorithm:
        Starting from the least significant bit, we enumerate each bit to determine which value is the majority at this bit,
    0 or 1, and put this value to the corresponding bit of the result. 
    Finally, we end up with the most least significant bit of all elements and return the result.
    """
    def majorityElement(self, nums: List[int]) -> int:
        


nums = [3,3,4]
# s = Solution()
# print(s.majorityElement(nums))

# b = BruteForce()
# print("BruteForce [O(N^2), O(1)]:", b.majorityElement(nums))

# m = HashMap()
# print("Dictionary [O(N), O(N)]:", m.majorityElement(nums))
# print(m.collec(nums))

s = Sorting()
print(s.majorityElement(nums))