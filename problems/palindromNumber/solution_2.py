""""
# info
palindrome number with a reversed sum

# results

Runtime: 80 ms, faster than 42.49% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 50.24% of Python3 online submissions for Palindrome Number.

# analysis

the solution runs in O(log_10(x)) for string convertion then another same for it's chekcing hence the total O(log_10(x))

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

    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        rev = self.reverse(x)

        return (rev+x) / 2 == x