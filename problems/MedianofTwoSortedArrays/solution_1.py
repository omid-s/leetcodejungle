
"""



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

