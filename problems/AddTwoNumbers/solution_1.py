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

        digit, carry = self.add_with_carry(l1.val, l2.val)
        l1 = l1.next
        l2 = l2.next

        ret_head = ListNode(digit)
        ret_tail = ret_head

        while l1 is not None and l2 is not None:
            digit, carry = self.add_with_carry(l1.val, l2.val, carry)
            l1 = l1.next
            l2 = l2.next

            digit_item = ListNode(digit)
            ret_tail.next = digit_item
            ret_tail = digit_item

        if l1 is not None:
            lst = l1
        else:
            lst = l2

        while lst is not None:
            digit, carry = self.add_with_carry(lst.val, 0, carry)
            lst = lst.next

            digit_item = ListNode(digit)
            ret_tail.next = digit_item
            ret_tail = digit_item

        if carry > 0:
            digit_item = ListNode(carry)
            ret_tail.next = digit_item

        return ret_head

    def add_with_carry(self, n1: int, n2: int, carry=0):
        """
        adds two single digit numbers and returns the result in term of a single digit and a carry
        :param n1: first number
        :param n2: second number
        :param carry: carry from previous steps
        :return: the digit, the carry
        """
        num = n1 + n2 + carry
        return num % 10, num // 10
