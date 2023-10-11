from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        dist = 0
        glo_min = arrays[0][0]
        glo_max = arrays[0][len(arrays[0])-1]
        for i in range(1, len(arrays)):
            arr = arrays[i]
            loc_min = arr[0]
            loc_max = arr[len(arr)-1]
            dist1 = abs(glo_min - loc_max)
            dist2 = abs(glo_max - loc_min)
            cur_dist = max(dist1, dist2)
            dist = max(dist, cur_dist)
            glo_min = min(glo_min, loc_min)
            glo_max = max(glo_max, loc_max)

        return dist
    
s = Solution()
arrays = [[1,2,3],[4,5],[1,2,3]]
dist = s.maxDistance(arrays)
print(dist)
