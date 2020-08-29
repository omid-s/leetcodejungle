from classes.ListNode import ListNode

"""
# Info 
removes  the nth to the end of a list in one pass

# Results

Runtime: 24 ms, faster than 98.54% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.8 MB, less than 67.09% of Python3 online submissions for Remove Nth Node From End of List.


# Anlaysis 
The linked list is travered exactly once to the end, thus the runtime is of O(n) where n is the 
length of the list. 
Space complexity is of O(n+1) as there is one new item created to handle pre-head node which makes
the solution of O(n) space as well. 

"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp_head = head
        n_1 = ListNode("")
        n_1.next = head
        cntr = 0

        while temp_head.next:
            cntr += 1
            if cntr >= n:
                n_1 = n_1.next

            temp_head = temp_head.next

        if n_1.next == head:
            head = head.next
        else:
            n_1.next = n_1.next.next

        return head