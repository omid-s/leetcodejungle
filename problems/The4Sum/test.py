from problems.The4Sum.solution_1 import Solution
from classes.Tools import array_equal

inputs = [
    [[1, 0, -1, 0, -2, 2], 0],
    [[-1, -5, -5, -3, 2, 5, 0, 4], -7],
    [[-7, -5, 0, 7, 1, 1, -10, -2, 7, 7, -2, -6, 0, -10, -5, 7, -8, 5], 28]

]
outputs = [
    [
        [-1, 0, 0, 1],
        [-2, -1, 1, 2],
        [-2, 0, 0, 2]
    ],
    [[-5, -5, -1, 4], [-5, -3, -1, 2]],
    [[7, 7, 7, 7]]

]

for index in range(len(inputs)):
    ret = Solution().fourSum(inputs[index][0], inputs[index][1])
    print(outputs[index], "-->", ret)
    assert array_equal(ret, outputs[index])

print("All tests passed")
