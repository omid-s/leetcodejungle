from problems.ValidPrantethies.solution_1 import Solution


inputs = [
"()",
"()[]{}",
"(]",
"([)]",
"{[]}"
]
outputs = [
    True,
    True,
    False,
    False,
    True
]

for index in range(len(inputs)):
    ret = Solution().isValid(inputs[index])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]

print("All tests passed")
