from problems.RegularExpressionLookup.solution_1_leetcode import Solution

inputs = [
    ["aa","a*"],
    ["ab", ".*"],
    ["aab", "c*a*b"],
    ["mississippi", "mis*is*p*."],
    ["meh","na*"],
    ["abcd",".*e"],
    ["ab", ".*c"],
    ["aaa", "aaaa"]

]

outputs = [
    True,
    True,
    True,
    False,
    False,
    False,
    False,
    False
]

for index in range(len(inputs)):
    ret = Solution().isMatch(inputs[index][0],inputs[index][1])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]

print("All tests passed")