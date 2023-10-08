from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(val = head[0], next=None)
        if len(head) == 1:
            return head
    
    def gcd(self, num1: int, num2: int) -> int:
        if num1 > num2:
            r = num1 % num2
            num2 % r 

            


s = Solution()
head = [18,6,10,3]
s.insertGreatestCommonDivisors(head)