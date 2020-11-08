"""

# Info

Removes repeated elements from the list in place.

# Results

Runtime: 8560 ms, faster than 5.02% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 91.79% of Python3 online submissions for Remove Duplicates from Sorted Array.

# Analysis


"""

class Solution:

    def move_left(self, arr, cnt, start, end):
        for i in range(start, end-cnt):
            arr[i] = arr[i+cnt]

    def removeDuplicates(self, nums) -> int:

        ret = len(nums)

        # base case
        if len(nums) < 2:
            return len(nums)
        i = 1
        while i < ret:
            cnt = 0
            while i+cnt < ret and nums[i + cnt] == nums[i-1]:
                cnt += 1

            if cnt > 0:
                self.move_left(nums, cnt, i, ret)
                ret -= cnt

            i += 1

        return ret
