
"""
# info

Sorts the array then iterrates over the array with narrowing window

# results :

Time Limit Excceded

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

        for x, v in enumerate(nums):
            if v > 0:
                break

            y = x+1
            z = len(nums) - 1

            while y < z:
                a = nums[x]
                b = nums[y]
                c = nums[z]
                sum = a + b + c

                if sum == 0 and [a,b,c] not in ret:
                    ret.append([a,b,c])
                    y += 1
                elif sum < 0 :
                    y += 1
                else:
                    z -= 1


        return ret
