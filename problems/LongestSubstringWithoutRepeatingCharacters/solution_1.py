"""
contains implementation for the longestUniqueSubString problem

#


"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        ret = 1

        sub_str = ""
        longest_str = ""

        for index in range(len(s)):
            the_char = s[index]

            if the_char in sub_str:
                sub_str = sub_str[sub_str.index(the_char)+1:]

            sub_str += the_char

            if len(longest_str) < len(sub_str):
                longest_str = sub_str

        ret = len(longest_str)

        return ret
