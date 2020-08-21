from problems.ReverseInt.solution_1 import Solution

inputs = [
    ["aa","a*"],
    ["ab", ".*"],
    ["aab", "c*a*b"],
    ["mississippi", "mis*is*p*."],
    ["meh","na*"]
]

outputs = [
    True,
    True,
    True,
    False,
    False
]

for index in range(len(inputs)):
    ret = Solution().reverse(inputs[index])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]

print("All tests passed")