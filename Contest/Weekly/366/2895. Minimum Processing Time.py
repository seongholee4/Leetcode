from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        l = len(processorTime)
        processorTime.sort()
        tasks.sort(reverse=True)
        print(processorTime,tasks)
        # if l == 1:
        #     return max(processorTime[0]+max(tasks))
        # if l == 2:
        #     return max(processorTime[0]+max(tasks[:4]), processorTime[1]+max(tasks[4:]))
        
        t = 0
        cur_max = 0
        for i in range(0, len(tasks), 4):
            cur_max = max(cur_max, processorTime[t]+max(tasks[i:i+4]))
            t+=1
        
        return cur_max
        # if l == 3:
        #     return max(processorTime[0]+max(tasks[:4]), processorTime[1]+max(tasks[4:8]), processorTime[2]+max(tasks[8:]))
        # if l == 4:
        #     return max(processorTime[0]+max(tasks[:4]), processorTime[1]+max(tasks[4:8]), processorTime[2]+max(tasks[8:12]), processorTime[3]+max(tasks[12:]))

s = Solution()
processorTime = [8,10]
tasks = [2,2,3,1,8,7,4,5]
# processorTime = [10,20]
# tasks = [2,3,1,2,5,8,4,3]
print(s.minProcessingTime(processorTime,tasks))
