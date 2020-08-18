"""
# info
a better implementation of the int reverse problem, this still assumes a bigger container for the integer, eg. the
integer is assumed to be more than 32 bits so that the inverse can fit in it

# results
Runtime: 32 ms, faster than 75.33% of Python3 online submissions for Reverse Integer.
Memory Usage: 14 MB, less than 6.44% of Python3 online submissions for Reverse Integer.

# analysis
the code runs in O(log_10(x))

"""

import math

class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        ret = 0

        x *= sign

        max_num = math.pow(2, 31)-1
        min_num = math.pow(-2, 31)

        while min_num < ret < max_num and x > 0:
            digit = x % 10
            ret = ret * 10 + digit

            x //= 10

        ret *= sign

        if min_num > ret or ret > max_num:
            ret = 0

        return ret
