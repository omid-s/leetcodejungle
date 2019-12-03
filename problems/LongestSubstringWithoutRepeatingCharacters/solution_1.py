"""
contains implementation for the longestUniqueSubString problem

# analysis

## Time :

    The solution passes once through the whole string but for each character it compares it with the previous substring
    as this can be in worst case of len(substr) = len(s) and best case of len(substr) = 1, we have to assume the runtime
    is of O(len(s)^2).

## Memory :

    Memory used to keep one copy of the string which is the substring and one copy of the longest substring is needed.
    this will create an O(len(s)) of space complexity

## To Improve:

    this problem can easily be done in O(len(s)) if search in the substring is replaced with a hash table implementation
    of the substring. Assuming a O(1) access in the hashtable implementation, we will have only one pass through the
    whole string thus the runtime will be of O(n)


# results

Runtime: 48 ms, faster than 97.84% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13 MB, less than 99.49% of Python3 online submissions for Longest Substring Without Repeating Characters.

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
