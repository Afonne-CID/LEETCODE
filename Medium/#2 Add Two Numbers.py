from typing import Optional

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_val, l2_val = '', ''
        while l1:
            l1_val += str(l1.val)
            l1 = l1.next
        while l2:
            l2_val += str(l2.val)
            l2 = l2.next
        sum = str(int(l1_val[::-1]) + int(l2_val[::-1]))[::-1]

        new = ListNode()
        cur = new

        for i in sum:
            new.next = ListNode(int(i))
            new = new.next
        return cur.next