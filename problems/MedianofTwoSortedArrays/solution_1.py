
"""
contains solution to Median of two sorted arrays problem

# Analysis

## Time

based on the length of the sequences the mid point is found, so only up to the midpoint is traversed, this makes this
solution an O( (l(a) + l(b)) /2) which is equal to O(l(a)+l(b))

## Space

This solution stores only three variables the current number, the past number and the counter, thus space complexity is
of O(1)

# Improvement

since both the sequences are known to be sorted a double binary search tree approach will reduce the complexity to an
O(log(l(a)+l(b))).

# Results

Runtime: 104 ms, faster than 74.01% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.

"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        index = (l1 + l2) / 2.0

        ctr = 0
        nums1_index = 0
        nums2_index = 0

        current_num = 0
        previous_num = 0

        while True:
            ctr += 1
            if nums1_index < l1 and nums2_index < l2:
                if nums1[nums1_index] < nums2[nums2_index]:
                    previous_num = current_num
                    current_num = nums1[nums1_index]
                    nums1_index += 1
                else:
                    previous_num = current_num
                    current_num = nums2[nums2_index]
                    nums2_index += 1

            elif nums1_index < l1 and nums2_index >= l2:
                previous_num = current_num
                current_num = nums1[nums1_index]
                nums1_index += 1

            elif nums1_index >= l1 and nums2_index < l2:
                previous_num = current_num
                current_num = nums2[nums2_index]
                nums2_index += 1

            if ctr > index:
                break

        if index % 1 == 0:
            return (current_num + previous_num) /2
        else:
            return current_num

