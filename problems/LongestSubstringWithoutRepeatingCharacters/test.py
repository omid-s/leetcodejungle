from problems.LongestSubstringWithoutRepeatingCharacters.solution_1 import Solution

inputs = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    "abkjsdh"
]

outputs = [
    3,
    1,
    3,
    7
]

for index in range(len(inputs)):
    s = inputs[index]

    ret = Solution().lengthOfLongestSubstring(s)

    print("%s : %d -> %d" % (s, outputs[index], ret))

    assert ret == outputs[index]

print("All tests passed")
