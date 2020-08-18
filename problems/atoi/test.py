from problems.atoi.solution_1 import Solution

inputs = [
    "45",
    "    45",
    " -410",
    "4193 with words",
    "words and 987",
    "-91283472332"
]

outputs = [
    45,
    45,
    -410,
    4193,
    0,
    -2147483648
]

for index in range(len(inputs)):
    ret = Solution().myAtoi(inputs[index])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]

print("All tests passed")
