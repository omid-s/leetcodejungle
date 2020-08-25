"""

# Info

This solution uses a recursive approach to stitch the parts of the combination to gether,

# Results

Runtime: 48 ms, faster than 21.00% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.8 MB, less than 79.50% of Python3 online submissions for Letter Combinations of a Phone Number.

# Analysis

it is a recursion of branch factor 3 except for 2 possbibiliteies where it has a 4, so the worstcase is approximately
 in O(4^n)

"""

class Solution:

    def letterCombinations(self, digits: str) :
        mappin = {"2":"abc",
                  "3":"def",
                "4":"ghi",
                  "5":"jkl",
                  "6":"mno",
                  "7":"pqrs",
                  "8":"tuv",
                  "9":"wxyz"
                 }

        ret = []

        if len(digits) == 0:
            return ret
        if len(digits) == 1:
            return list(mappin[digits[0]])

        temp = self.letterCombinations(digits[1:])

        for x in mappin[digits[0]]:
            for y in temp:
                ret.append(x+y)

        return ret
