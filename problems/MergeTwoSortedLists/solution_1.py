from classes.ListNode import ListNode

"""
# Info 

This merges the lists in place with just one head and tail variabels added 

# Results
Runtime: 40 ms, faster than 59.03% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.8 MB, less than 78.56% of Python3 online submissions for Merge Two Sorted Lists.

# Analysis

The algorithm runs through each list once at most (if a one list is finished faster, it will use just one operation
for the other list). so Given the l1 and l2 of length |l1| and |l2| we have an runtime complexity of O(|l1|+|l2|) and
a space complexity of O(|l1|+|l2|) in total. 

"""


class Solution:

    def set_head_and_tail(self, node, head, tail):
        """
        sets the head and tail
        :param node: the node to be added
        :param head: head of the list
        :param tail: tail of the list
        :return: new head, tail
        """
        if head is None:
            head = node
        else:
            tail.next = node

        tail = node
        return head, tail

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None

        while l1 and l2:
            if l1.val <= l2.val:
                head, tail = self.set_head_and_tail(l1, head, tail)
                l1 = l1.next
            else:
                head, tail = self.set_head_and_tail(l2, head, tail)
                l2 = l2.next
        if l1:
            head, tail = self.set_head_and_tail(l1, head, tail)
        if l2:
            head, tail = self.set_head_and_tail(l2, head, tail)

        return head
