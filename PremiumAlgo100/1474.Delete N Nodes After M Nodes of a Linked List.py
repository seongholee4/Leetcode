# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        # keep the first m nodes
        # i.e. jump to m+1 nodes
        curNode = head
        while curNode is not None:
            for i in range(0,m-1):
                if curNode is not None:
                    curNode = curNode.next
            a = curNode
            for i in range(0,n+1):
                # jump to n+1 node
                if curNode is not None:
                    curNode = curNode.next
            if a is not None:
                a.next = curNode

        return head

s = Solution()
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
head = ListNode(arr[0])
current = head
for val in arr[1:]:
    current.next = ListNode(val)
    current = current.next
m = 2
n = 3
new_node = s.deleteNodes(head, m, n)
def iterate_linked_list(head):
    current = head  # Start at the head of the linked list

    while current is not None:
        # Process the current node
        print(current.val)

        # Move to the next node
        current = current.next

iterate_linked_list(new_node)
