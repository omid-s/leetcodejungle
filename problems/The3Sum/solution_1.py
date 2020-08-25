
"""
# info

This solution is the bruteforce way, it itterats over all item combinations

# results :

Time Limit Excceded

# analysis

the solution runs n*(n-1)*(n-2) times, hence it's in O(n^3)

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

        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    a= nums[x]
                    b= nums[y]
                    c= nums[z]

                    if a+b+c == 0 and [a,b,c] not in ret:
                        ret.append(sorted([a, b, c]))


        return ret
