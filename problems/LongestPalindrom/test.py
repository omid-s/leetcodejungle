from problems.LongestPalindrom.solution_1 import Solution

inputs = [
    "abccbab",
    "bbbbb",
    "pwwkew",
    "sdhabba",
    "miokoim"
]

outputs = [
    "abc",
    "bbbbb",
    "ww",
    "abba",
    "miokoim"
]

for index in range(len(inputs)):
    s = inputs[index]

    ret = Solution().longestPalindrome(s)

    print("%s : %s -> %s" % (s, outputs[index], ret))

    assert ret == outputs[index]

print("All tests passed")
