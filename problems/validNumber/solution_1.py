"""
info :



resutls :

Runtime: 48 ms, faster than 12.06% of Python3 online submissions for Valid Number.
Memory Usage: 14.2 MB, less than 86.13% of Python3 online submissions for Valid Number.

analysis :


the solution runs in an O(n) runtime and O(n) space complexity. the time compexity coeficeitn can be reduced

"""


class Solution:
    def is_digit_number(self, c):
        return c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    def check_length(self, x):
        return len(x) >= 1

    def is_integer(self, x):
        """
        checks if a number complies with Integer rules
        """

        if not self.check_length(x):
            return False

        if x[0] in ['-', '+']:
            x = x[1:]

        if not self.check_length(x):
            return False

        for i, c in enumerate(x):
            if not self.is_digit_number(c):
                return False
        return True

    def is_decimal(self, x):
        if not self.check_length(x):
            return False
        if x[0] in ['-', '+']:
            x = x[1:]
        if not self.check_length(x):
            return False

        dot_seen = False
        for i, c in enumerate(x):
            if c in ['-', '+']:
                return False
            if c == '.':
                if dot_seen:
                    return False
                else:
                    dot_seen = True
                continue

            if not self.is_digit_number(c):
                return False
        return not (dot_seen and len(x) == 1)

    def isNumber(self, s: str) -> bool:
        s = s.lower()
        e_ind = s.index('e') if 'e' in s else -1
        if e_ind < 0:
            return self.is_integer(s) or self.is_decimal(s)
        else:
            return (self.is_integer(s[:e_ind]) or self.is_decimal(s[:e_ind])) and self.is_integer(s[e_ind + 1:])