from problems.The3SumClosest.solution_1 import Solution
from classes.Tools import array_equal

inputs = [
    [[-1, 2, 1, -4], 1],
    [[1,1,1,1], 0],
    [[1,1,1,0],100],
    [[0,2,1,-3],1]

]
outputs = [
    2,
    3,
    3,
    0
]

for index in range(len(inputs)):
    ret = Solution().threeSumClosest(inputs[index][0], inputs[index][1])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]

print("All tests passed")
