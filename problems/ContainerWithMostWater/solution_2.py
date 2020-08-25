"""

# info

This is a more optimized solution, we are optimizing based on 2 variables, so starting with a max width
and going lower we can pursue a greedy approach to the problem.

# Results

Runtime: 212 ms, faster than 17.76% of Python3 online submissions for Container With Most Water.
Memory Usage: 15.4 MB, less than 61.96% of Python3 online submissions for Container With Most Water.

# Analysis

this runs in O(N) where N is the length of the sequence
"""


class Solution:

    def get_volume(self, x, y):
        w = x[0] - y[0]
        h = min(x[1], y[1])
        return abs(w * h)

    def maxArea(self, height) -> int:
        max_vol = 0
        i = 0
        j = len(height)-1

        while i != j:
            vol = self.get_volume((i, height[i]), (j, height[j]))
            if vol > max_vol:
                max_vol = vol
            if height[i]< height[j]:
                i += 1
            else:
                j -= 1

        return max_vol
