from problems.IntToRoman.solution_1 import Solution

inputs = [
    3,
    4,
    1994,
    58
]

outputs = [
    "III",
    "IV",
    "MCMXCIV",
    "LVIII"
]

for index in range(len(inputs)):
    ret = Solution().intToRoman(inputs[index])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]


print("All tests passed")
