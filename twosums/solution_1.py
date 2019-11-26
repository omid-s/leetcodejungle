"""
the stupid implementation, this is a baseline with O(n^2) to be more exact O( sum(i*(i-1)) for i = 0-n )


Runtime: 6496 ms, faster than 5.03% of Python3 online submissions for Two Sum.
Memory Usage: 13.7 MB, less than 77.21% of Python3 online submissions for Two Sum.


"""


class Solution:
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]
        return []
