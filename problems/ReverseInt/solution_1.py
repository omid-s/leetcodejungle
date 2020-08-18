"""
# info
naive implementation for the integer reverse problem, this uses the string convertor functions, eg. literally cheating
:D

# results

Runtime: 16 ms, faster than 99.97% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.9 MB, less than 32.07% of Python3 online submissions for Reverse Integer.


# analysis
this code runs at O(log_10(n)) + O(python itoa function).

"""

import math


class Solution:
    def reverse(self, x: int) -> int:

        thestr = str(x)
        sign = x < 0
        ret = ""
        cntr = 0
        # if negative skip the first char
        if sign:
            cntr += 1

        while cntr < len(thestr):
            ret = thestr[cntr] + ret
            cntr += 1

        if sign:
            ret = "-" + ret

        ret = int(ret)
        if ret > (math.pow(2, 31) - 1) or ret < math.pow(-2, 31):
            ret = 0

        return ret
