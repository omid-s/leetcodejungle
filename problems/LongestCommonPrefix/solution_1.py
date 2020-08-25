"""
# Info

just itterates over the strings as long as they have common sub string

# Results

Runtime: 28 ms, faster than 94.98% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.9 MB, less than 56.10% of Python3 online submissions for Longest Common Prefix.

# Analysis

it passes through each string L times at most, where L is the length of the shortest string. if we have N strings
the solution will run in O(LN)

"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # check initial criteria
        if len(strs) == 0 or "" in strs:
            return ""

        lcp = ""
        index = 0
        while True:
            flag = False

            for x in strs:
                if len(x) <= index:
                    flag = True
                    break

            if flag:
                break

            c = strs[0][index]

            for x in strs:
                if c != x[index]:
                    c = ""
                    break

            index += 1
            if flag or c == "":
                break
            lcp += c

        return lcp