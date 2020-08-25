"""
# info

Sorts the array then iterrates over the array with narrowing window.

# results :

Runtime: 1064 ms, faster than 46.34% of Python3 online submissions for 4Sum.
Memory Usage: 14 MB, less than 39.19% of Python3 online submissions for 4Sum.

# analysis

the solution runs O(nlogn) + O(n^3) times, hence it's in O(n^3)

"""


class Solution:
    def fourSum(self, nums, target: int):

        if len(nums) < 4:
            return []

        # sort the array
        nums = sorted(nums)

        ret = []

        d_prev = float('inf')
        for w, d in enumerate(nums):

            if d == d_prev:
                continue
            else:
                d_prev = d

            a_prev = float('inf')
            for x in range(w + 1, len(nums)):
                a = nums[x]

                if a == a_prev:
                    continue
                else:
                    a_prev = a

                y = x + 1
                z = len(nums) - 1

                while y < z:

                    b = nums[y]
                    c = nums[z]

                    sum = a + b + c + d

                    if sum == target:
                        ret.append([d, a, b, c])
                        while y < len(nums) and nums[y] == b:
                            y += 1

                    if sum < target:
                        y += 1
                    else:
                        z -= 1

        return ret
