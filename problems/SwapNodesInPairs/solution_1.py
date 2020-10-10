from classes.Tools import str2LinkedList
from classes.Tools import *
from classes.ListNode import ListNode

"""
# Info 

This swaps the two nodes by changing the place of the next and previous items. 

# Results

Runtime: 48 ms, faster than 11.32% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14.2 MB, less than 99.99% of Python3 online submissions for Swap Nodes in Pairs.

# Analysis

the loop iterates for every other element on the list so it has a runtime of O(n), as for space complexity, it does
not change the list structure, it just adds one more node, hence the space is of O(n+1)

"""


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ret_head = None
        prev = ListNode(0)

        if not head:
            return head

        tail = head
        next = head.next

        cntr = 0
        while next:
            # make the move
            prev.next = next

            tail.next = next.next
            next.next = tail

            if ret_head is None:
                ret_head = next

            prev = tail
            tail = tail.next
            next = tail.next if tail else None

        return ret_head if ret_head else head
