class Solution:

    def move_left(self, arr, n, start):
        for i in range(start, len(arr)):
            arr[i - n] = arr[i]

    def move_left_simple(self, arr, index):
        for i in range(index, len(arr)):
            arr[i - 1] = arr[i]

    def removeDuplicates(self, nums) -> int:
        begin_index = -1
        index = 0
        deleted = 0

        ret = len(nums)
        # base case
        if len(nums) < 2:
            return len(nums)
        i = 1
        while i < ret:
            if nums[i - 1] == nums[i]:
                self.move_left_simple(nums, i)
                ret -= 1
                i -= 1
            i += 1

        return ret
