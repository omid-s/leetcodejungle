"""
# Info

The recursive. This solution starts by the only valid string for length 1 which is '(' then in the consecutive steps
it adds bth '(' and ')', this helps with keep growing only valid sequences.

# results

Runtime: 36 ms, faster than 58.35% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.2 MB, less than 36.34% of Python3 online submissions for Generate Parentheses.


# Analysis

this creates a recursion tree of branch factor 2 and depth 2n, this means the worst case for the algorithem is
going to run in O(2^2n) but the vast majority of branches will be cut early, so this is not a tight bound. a tighter
bound can be calculated by calculating P(fail| sequence length) and multiplying that to the overall time.

"""


class Solution:
    def make_parenthesis(self, seq, o, c):
        """
        generates a set of parantethesis,
        :param seq: the current sequence
        :param o: number of open brackets left
        :param c: number of close brackets left
        :return: an array of bracket strings
        """
        ret = []
        # base case check, the closed brackets can nbever be less than the open ones.
        if c < o or o < 0:
            return []

        if o == 0 and c == 0:
            return [seq]

        ret.extend(self.make_parenthesis(seq + '(', o - 1, c))
        ret.extend(self.make_parenthesis(seq + ')', o, c - 1))

        return ret

    def generateParenthesis(self, n: int):
        return self.make_parenthesis("(", n - 1, n)
