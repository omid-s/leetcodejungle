"""
# info

Sorts the array then iterrates over the array with narrowing window. This version introduces improvements over solution2
in terms of finding repeated work

# results :

Runtime: 1560 ms, faster than 28.88% of Python3 online submissions for 3Sum.
Memory Usage: 17.1 MB, less than 82.57% of Python3 online submissions for 3Sum.

# analysis

the solution runs O(nlogn) + O(n^2) times, hence it's in O(n^2)

"""


class Solution:
    def threeSum(self, nums):

        if len(nums) < 3:
            return []

        # sort the array
        nums = sorted(nums)

        # verify there is a possibility for a solution
        if nums[0] * nums[-1] > 0:
            return []

        ret = []

        v_prev = 500
        for x, v in enumerate(nums):
            if v > 0:
                break
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

                if sum == 0:
                    ret.append([a, b, c])
                    while y < len(nums) and nums[y] == b:
                        y += 1

                elif sum < 0:
                    y += 1
                else:
                    z -= 1

        return ret
