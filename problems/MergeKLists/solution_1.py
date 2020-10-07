from classes.ListNode import ListNode

""""
# Info 

This is a base solution, this loops inthe list every time it adds one node. This can be farther improved if an insertion
sort mechanism is put in place instead of a naive loop every time. 

# Results 

Runtime: 4260 ms, faster than 10.60% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.4 MB, less than 86.80% of Python3 online submissions for Merge k Sorted Lists.


# Analysis

Assuming there are n lists and a total of m nodes, the runtime complexity has an upper bound of O(n*m) because for each
item added to the list we traverse all the lists. 
Space complexity on the other hand vecause it has no added space needs, is O(m)

"""

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        ret_head = None
        ret_tail = None

        while len(lists) > 0:
            min_ind = 0
            min_val = 9999999999999
            for i, x in enumerate(lists):
                if x and x.val <= min_val:
                    min_ind = i
                    min_val = x.val

            if lists[min_ind]:
                if ret_tail:
                    ret_tail.next = lists[min_ind]
                    ret_tail = lists[min_ind]
                else:
                    ret_tail = lists[min_ind]
                    ret_head = ret_tail

                lists[min_ind] = lists[min_ind].next


            if lists[min_ind] is None:
                del lists[min_ind]

        return ret_head
