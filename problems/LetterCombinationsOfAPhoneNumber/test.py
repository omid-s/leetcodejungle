from problems.LetterCombinationsOfAPhoneNumber.solution_1 import Solution
from classes.Tools import array_equal


inputs = [
    "23",
]
outputs = [
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
]


for index in range(len(inputs)):
    ret = Solution().letterCombinations(inputs[index])
    print(outputs[index], "-->", ret)
    assert array_equal(ret, outputs[index])


print("All tests passed")
