from problems.The3Sum.solution_2 import Solution
from classes.Tools import array_equal

inputs = [
    [-1, 0, 1, 2, -1, -4],
    [0, 0, 0],
    [-1, 0, 1],
    [0, 0, 0, 0]
]
outputs = [
    [
        [-1, 0, 1],
        [-1, -1, 2]
    ],
    [[0, 0, 0]],
    [[-1, 0, 1]],
    [[0, 0, 0]]

]

for index in range(len(inputs)):
    ret = Solution().threeSum(inputs[index])
    print(outputs[index], "-->", ret)
    assert array_equal(ret, outputs[index])

print("All tests passed")
