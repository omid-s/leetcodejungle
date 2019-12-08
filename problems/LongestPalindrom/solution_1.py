"""
contains implementation for the longest palindrome in a string

# Analysis

## Time

the first for loop, itterrates over all the chars in the string, then if there is a similarity around the current index,
it will find the polindrom around the area. Finding a polindrom around an index is of worst case O(len(S)) how ever,
there is only exactly one time it can reach len(n) checks and that is when index is equal to len(S)/2. The total runtime
is subsequently of O(len(S)^2)

## Space

In each round only the palindromes are kept in memory plus some indexes. A palindrome can be of a maximum length equal
 to len(S) thus the memory is of O(len(S))


# improvements

no idea so far :D 

# Results

Runtime: 3332 ms, faster than 38.09% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13 MB, less than 97.48% of Python3 online submissions for Longest Palindromic Substring.

"""
import math


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 0:
            return ""
        else:
            ret = s[0]

        for index in range(len(s)-1):
            if s[index] == s[index+1]:
                temp = self.polindrom_from(s, index+0.5)
                if len(temp) > len(ret):
                    ret = temp
            if index >= 1 and s[index-1] == s[index+1]:
                temp = self.polindrom_from(s, index)
                if len(temp) > len(ret):
                    ret = temp

        return ret

    def polindrom_from(self, s: str, index):
        i = 0
        ret = s[math.floor(index): math.ceil(index)+1]

        while True:
            i += 1
            b_index = math.floor(index - i)
            a_index = math.ceil(index + i)

            if b_index < 0 or a_index >= len(s):
                break;

            if s[b_index] == s[a_index]:
                ret = "%s%s%s" % (s[b_index], ret, s[a_index])
            else:
                break

        return ret
