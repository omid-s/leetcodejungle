"""
this class is an implementation of the AddTwoNumbers problem in leet code

# Analysis

This solution traverses each of the lists once, and only stores the return list.

## Time

each node in the list is traversed eactly once, thus the running time is O(|l1| + |l2|) where "|" shows the length.

## space

only one extra list is created, this list is of order O(max(|l1|, |l2|) + 1) this happens because the last number may
produce carry overs.

"""

from classes.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return None