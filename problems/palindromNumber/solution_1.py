""""
# info

# results

Runtime: 112 ms, faster than 14.77% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 31.26% of Python3 online submissions for Palindrome Number.

# analysis
the solution runs in O(log_10(x)) for string convertion then another same for it's chekcing hence the total O(log_10(x))
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        the_str = str(x)

        for i in range(len(the_str)//2):
            if the_str[i] != the_str[-1 * (i+1)]:
                return False

        return True