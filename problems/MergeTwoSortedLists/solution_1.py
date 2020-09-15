from classes.ListNode import ListNode

"""
# Info 

# Results

# Analysis

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
