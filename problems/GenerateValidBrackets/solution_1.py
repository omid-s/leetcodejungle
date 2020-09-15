"""
# Info

The Ugly bruteForth solution, this solution creates all the combinations of the paranthesis and then validates them
all. the ones that are not valid will be terminated

# results

Time Limit Error :D


# Analysis
Solution need O(2n) for checking each answer candidate, the combination part runs in O(n!).. so an overall of O(n.n!)
not so fun huh :D

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

    def combination(self, string, items):
        ret = []
        if len(items) == 0:
            return [string]

        for i in range(len(items)):
            tmp = list(items)
            del(tmp[i])
            ret.extend(self.combination(string+items[i], tmp))
        return ret

    def generateParenthesis(self, n: int):
        ret = []
        the_list = []
        for i in range(n):
            the_list.append("(")
            the_list.append(")")

        candidates = list(set(self.combination("", the_list)))

        i = 0
        while i < len(candidates):
            if not self.isValid(candidates[i]):
                del(candidates[i])
                i -= 1
            i += 1

        return candidates

