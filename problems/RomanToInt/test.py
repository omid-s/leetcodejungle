from problems.RomanToInt.solution_1 import Solution

inputs = [
    "III",
    "IV",
    "MCMXCIV",
    "LVIII"
]
outputs = [
    3,
    4,
    1994,
    58
]

for index in range(len(inputs)):
    ret = Solution().romanToInt(inputs[index])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]


print("All tests passed")
