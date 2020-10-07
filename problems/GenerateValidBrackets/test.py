from problems.GenerateValidBrackets.solution_2 import Solution
from classes.Tools import array_equal


inputs = [
    1,
    2,
    3
]
outputs = [
    ["()"],
    ["()()", "(())"],
    [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]

]

for index in range(len(inputs)):
    ret = Solution().generateParenthesis(inputs[index])
    print(outputs[index], "-->", ret)
    assert array_equal(ret, outputs[index])


print("All tests passed")
