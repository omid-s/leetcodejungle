"""
# Info
This solution expands the symbol list and uses the sorted list as a refrence

# results

Runtime: 68 ms, faster than 35.66% of Python3 online submissions for Integer to Roman.
Memory Usage: 13.9 MB, less than 38.71% of Python3 online submissions for Integer to Roman.

# analysis

none of the symbols can be present more than 3 times except for `M` and we do one calculation per
each symbol so the runtime is of O(len(symbols)) which is of O(1).
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [
            ("I", 1),
            ("IV", 4),
            ("V", 5),
            ("IX", 9),
            ("X", 10),
            ("XL", 40),
            ("L", 50),
            ("XC", 90),
            ("C", 100),
            ("CD", 400),
            ("D", 500),
            ("CM", 900),
            ("M", 1000),
        ]
        ret = ""
        for i in range(len(symbols) - 1, -1, -1):
            m = num // symbols[i][1]
            ret += m * symbols[i][0]
            num %= symbols[i][1]

        return ret
