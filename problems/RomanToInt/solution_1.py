"""
# Info
This solution expands the symbol list and uses the sorted list as a refrence

# results

Runtime: 144 ms, faster than 6.28% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.8 MB, less than 79.21% of Python3 online submissions for Roman to Integer.

# analysis

assuming all sysmbols are of one character lenght the solution will be on O(len(symbols) * len(num)) which
can be simplified to O(len(num))

"""


class Solution:
    def romanToInt(self, num: str) -> str:
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
        ret = 0
        while len(num) > 0:
            for i in range(len(symbols) - 1, -1, -1):
                if len(num) == 0 :
                    break

                if num.startswith(symbols[i][0]):
                    ret += symbols[i][1]
                    num = num[len(symbols[i][0]):]

        return ret
