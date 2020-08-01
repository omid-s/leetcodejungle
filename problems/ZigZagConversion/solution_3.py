
"""
# Info

# Results

Runtime: 48 ms, faster than 97.88% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 14 MB, less than 19.13% of Python3 online submissions for ZigZag Conversion.

# Analysis

This solution still works at a O(l) but the space is of O(l) as well. Also the string calculations have been reduced
drastically.
"""

class Solution:
    def convert(self, s: str, numRows: int):

        # the first corner case : all text in one row
        if numRows == 1:
            return s

        l = len(s)

        temp = ["" for x in range(numRows)]

        # keep a count of the characters which are done
        cntr = 0
        j = 0
        mplier = 1
        while cntr < l:
            temp[j] += s[cntr]
            cntr += 1
            j += mplier
            if j == -1 or (j == numRows and mplier > 0):
                mplier *= -1
                j += 2*mplier

        temp = ''.join(temp)

        return temp

