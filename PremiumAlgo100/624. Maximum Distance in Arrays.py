from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        dist = 0
        i = 0
        # find 
        for i in range(len(arrays) - 1):
            # pick two arrays from list of arrays
            arr1 = arrays[i]
            for j in range(i + 1, len(arrays)):
                arr2 = arrays[j]
                # 1. calc distance between the min of arr1 and the max of arr2
                dist1 = abs(arr1[0] - arr2[len(arr2)-1])
                # 2. calc distance between the min of arr2 and the max of arr1
                dist2 = abs(arr1[len(arr1)-1] - arr2[0])
                # 2 - 1. extract max between dist1 and dist2
                cur_dist = max(dist1, dist2)
                # 3. update dist to be the global maximum.
                dist = max(cur_dist, dist)
                # 4. add 1 to i to move on to the next sequence.
                i += 1
        
        return dist


s = Solution()
arrays = [[2, 3], [1, 5], [2, 3]] # expected: 5 -2 = 3
arrays = [[1,2,3], [4,5], [1,2,3]] # expected: 5 - 1 = 4
arrays = [[1],[1]] # expected: 1 - 1 = 0
arrays = [[-1,5],[1,4,6],[4,5,6]]
arrays = [[7],[49],[73],[58],[30],[72]]
print(s.maxDistance(arrays))
# the first problem lied when both glo_min and glo_max are present in the same array.
# the second problem lied not going through all the array combinations in the arrays. (it was not like comparing between the arrays of 1,2 1,3 2,3)
# the third problem lied by time limit exceeding... (trying to resolve: n^2 -> nlogn)