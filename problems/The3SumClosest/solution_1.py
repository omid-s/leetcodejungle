"""
# info

This is the same implementation for 3sums with some different criterias.

Sorts the array then iterrates over the array with narrowing window. This version introduces improvements over solution2
in terms of finding repeated work

# results :

Runtime: 472 ms, faster than 11.15% of Python3 online submissions for 3Sum Closest.
Memory Usage: 14.1 MB, less than 9.11% of Python3 online submissions for 3Sum Closest.

# analysis

the solution runs O(nlogn) + O(n^2) times, hence it's in O(n^2)

"""


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:

        # sort the array
        nums = sorted(nums)

        # verify there is a possibility for a solution
        # if nums[0] * nums[-1] > 0:
        #     return []

        ret = 10000000

        v_prev = 500
        for x, v in enumerate(nums):

            if v == v_prev:
                continue
            else:
                v_prev = v

            y = x + 1
            z = len(nums) - 1

            while y < z:
                a = nums[x]
                b = nums[y]
                c = nums[z]
                sum = a + b + c

                dif = abs(sum - target)

                if dif < abs(ret-target):
                    ret = sum
                    # while y < len(nums) and nums[y] == b:
                    #     y += 1

                if sum < target:
                    y += 1
                else:
                    z -= 1

        return ret
