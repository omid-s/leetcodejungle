from classes.ListNode import ListNode
"""
# Info 
this solution first finds the items which have to be flipped and then they are flipped using another function, keeping
the last and first nodes in the cutrent and next K lists constant

# Results 

Runtime: 36 ms, faster than 99.80% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15 MB, less than 99.57% of Python3 online submissions for Reverse Nodes in k-Group.


# Analysis 
 The solution travels through all the nodes once. For each K nodes, it does a reordering, hence the over all runtime 
 will be of O(2n) = O(n). The space complexity can be calculated based on the fact that at each time there is a new
 list of K pointers to the nodes, this consumes a O(K) space. 
 
 # Improvements 
 
 In order to get this solution to O(1) space complexity, one can keep the reversing procedure inside the list by 
 a reverse itteration of the nodes from head and tail 



"""

class Solution:
    def find_k_set(self, head, k):
        cntr = 0
        ret = []
        while cntr < k and head:
            cntr += 1
            ret.append(head)
            head = head.next

        if cntr < k:
            return None, None

        return ret, head

    def reverse(self, the_list, prev):
        next_node = the_list[-1].next
        for i in range(len(the_list)-1, 0, -1):
            the_list[i].next = the_list[i-1]

        prev.next = the_list[-1]
        the_list[0].next = next_node

        return the_list[-1], the_list[0]

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        prev = ListNode(0)
        ret_head = None

        while True:
            to_flip, head = self.find_k_set(head, k)

            if to_flip:
                temp_head, prev = self.reverse(to_flip, prev)
                if not ret_head:
                    ret_head = temp_head

            else:
                break

        return ret_head