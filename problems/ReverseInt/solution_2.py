"""
# info
a better implementation of the int reverse problem

# results


# analysis

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
