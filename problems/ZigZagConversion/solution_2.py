"""
# info
The second solution to the problem, this will try to itterate a zigzag pattern on an array and put in the characters,
 but will try to conserve space and computations by just appending to a sequence instead of creating a big one


# Results

yeah this has a bug :D ABC,2 input does not work! the reason is the j=0 is a complecated case for this loop model
# Analysis


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
        i = 0
        j = 0

        while cntr < l:
            while j < numRows and cntr < l:
                temp[j]+=s[cntr]
                cntr += 1
                j += 1
            j -= 1
            while j > 0 and cntr < l:
                i += 1
                j -= 1
                temp[j]+=s[cntr]
                cntr += 1

            if cntr < l:
                cntr -= 1

        for x in temp:
            print(x)
        temp = ''.join(temp)


        return temp

