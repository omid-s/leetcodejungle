"""
# Info


# Results

# Analysis

"""

import math


class Solution:
    max_int = int(math.pow(2, 31) - 1)
    min_int = int(math.pow(-2, 31))

    def is_over_flowing(self, num, digit, sign):
        return not (self.max_int - sign * digit) / 10 > sign * num > (self.min_int - sign * digit) / 10

    def myAtoi(self, str: str) -> int:
        isValid = True
        ovf = False
        sign_seen = False
        ret = 0
        sign = 1
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for i in range(len(str)):
            if not sign_seen and str[i] == ' ':
                continue

            if not sign_seen:
                if str[i] == '-':
                    sign = -1
                    sign_seen = True
                elif str[i] == "+":
                    sign_seen = True
                elif str[i] in numbers:
                    sign_seen = True
                    ret = numbers.index(str[i])
                else:
                    isValid = False
                    break
                continue

            else:
                if str[i] in numbers:
                    digit = numbers.index(str[i])
                    if not self.is_over_flowing(ret, digit, sign):
                        ret = ret * 10 + digit
                    else:
                        ovf = True
                else:
                    break

        if ovf:
            if sign < 0:
                return self.min_int
            else:
                return self.max_int

        ret *= sign
        return ret
