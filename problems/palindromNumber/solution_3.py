""""
# info
palindrome number with a reversed sum

# results

Runtime: 84 ms, faster than 37.80% of Python3 online submissions for Palindrome Number.
Memory Usage: 14 MB, less than 10.03% of Python3 online submissions for Palindrome Number.

# analysis

the solution runs in O(log_10(x)/2)

"""

import math


class Solution:

    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        l = int(math.log10(x)) + 1

        high = math.pow(10, l - 1)
        low = 10

        for i in range(int(l // 2)):

            if (x // high) % 10 != (x % low) // (low / 10):
                return False
            high /= 10
            low *= 10

        return True
