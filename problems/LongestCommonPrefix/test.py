from problems.LongestCommonPrefix.solution_1 import Solution

inputs = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"]
]
outputs = [
    "fl",
    ""
]

for index in range(len(inputs)):
    ret = Solution().longestCommonPrefix(inputs[index])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]


print("All tests passed")
