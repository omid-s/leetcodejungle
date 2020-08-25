""""
# Info
    Brute force implementation of the solution

# Results

Time Limit Exceeded

# Analysis

This solution runs a c(2,N) with index removal it can be devided by two but still runs in a O(n^2)

"""


class Solution:

    def get_volume(self, x, y):
        w = x[0] - y[0]
        h = min(x[1], y[1])
        return abs(w * h)

    def maxArea(self, height) -> int:
        max_vol = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                vol = self.get_volume((i, height[i]), (j, height[j]))
                if vol > max_vol:
                    max_vol = vol
        return max_vol
