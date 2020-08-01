"""
# info
The first solution to the problem, this will try to itterate a zigzag pattern on an array and put in the characters


# results
Runtime: 2576 ms, faster than 5.02% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 23.6 MB, less than 5.06% of Python3 online submissions for ZigZag Conversion.

# analysis
This solution's main loop runs in O(l) where l is the length of the sequence. Space Complexity is in theory of O(l*l);
however the python implementation of joins and the sorts makes it more space and time consuming.

"""


class Solution:
    def convert(self, s: str, numRows: int):

        # the first corner case : all text in one row
        if numRows == 1:
            return s

        l = len(s)

        temp = [[' ' for x in range(l)] for x in range(l)]

        # keep a count of the characters which are done
        cntr = 0
        i = 0
        j = 0

        while cntr < l:
            while j < numRows and cntr < l:
                temp[j][i] = s[cntr]
                cntr += 1
                j += 1
            j -= 1
            while j > 0 and cntr < l:
                i += 1
                j -= 1
                temp[j][i] = s[cntr]
                cntr += 1
            if cntr < l:
                cntr -= 1

        temp = [''.join(x) for x in temp]
        temp = ''.join(temp)
        temp = temp.replace(" ", "")

        return temp

