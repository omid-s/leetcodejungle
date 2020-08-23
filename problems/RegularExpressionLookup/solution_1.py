"""
# Info

# Results

# Analysis


"""


class Solution:

    def find_states(self, p):
        ret = [x for x in p]
        i =0

        while i < len(ret)-1:
            if ret[i+1] == '*':
                ret[i] += '*'
                del(ret[i+1])
            i += 1

        return ret

    def match_token(self, s, p):
        match = False
        s_inc = 0
        p_inc = 0

        if p == '.':
            match = True
            p_inc = 1
            s_inc = 1

        elif p == '.*':
            match = True
            p_inc = 0
            s_inc = 1

        elif len(p) > 1 and p[0] == s:
            match = True
            p_inc = 0
            s_inc = 1

        elif len(p) > 1 and p[0] != s:
            match = True
            s_inc = 0
            p_inc = 1

        elif p == s:
            match = True
            s_inc = 1
            p_inc = 1

        return match, s_inc, p_inc


    def match(self, s:str, p_segments:list)-> bool:
        s_index = 0
        p_index = 0

        while s_index < len(s) and p_index < len(p_segments):

            match, s_inc, p_inc = self.match_token(s[s_index], p_segments[p_index])

            s_index += s_inc
            p_index += p_inc

            if not match:
                return False

        return s_index == len(s), p_index

    def isMatch(self, s: str, p: str) -> bool:
        s_index = 0
        p_index = 0

        if len(s) < 1:
            return True

        p_segments = self.find_states(p)

        forward, f_cntr = self.match(s, p_segments)
        backward, b_cntr = self.match(s[::-1], p_segments[::-1])

        return forward and backward