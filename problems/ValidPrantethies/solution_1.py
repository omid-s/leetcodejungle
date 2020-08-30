"""

# Info

validates the open/close parantesises in the gives sequence using stack.
this same thing can be done using recursion, or counters for each of the bracket types.

# Results

Runtime: 24 ms, faster than 95.12% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.8 MB, less than 79.44% of Python3 online submissions for Valid Parentheses.

# Analysis

The loop passes through the string at most once- best case scenario is early termination in
the first character. thus the runtime is of O(n).
The solution uses an stack which will grow to at most n/2 where n is the length of the input
string. thus space is of O(n) as well.

"""


class Solution:

    def push(self, stack, item):
        stack.append(item)

    def pop(self, stack):
        if len(stack) > 0:
            return stack.pop()
        else:
            return None

    def is_open(self, char):
        return char in ['(', '[', '{']

    def is_match(self, char1, char2):
        ret = False

        if char1 == char2:
            ret = False
        elif char1 == "[" and char2 == ']':
            ret = True
        elif char1 == "(" and char2 == ')':
            ret = True
        elif char1 == "{" and char2 == '}':
            ret = True

        return ret

    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if self.is_open(s[i]):
                self.push(stack, s[i])
            else:
                item = self.pop(stack)
                if not item or not self.is_match(item, s[i]):
                    return False

        return len(stack) == 0
