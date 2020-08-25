from problems.The3Sum.solution_1 import Solution

inputs = [
    [-1, 0, 1, 2, -1, -4],
    [0,0,0]
]
outputs = [
    [
        [-1, 0, 1],
        [-1, -1, 2]
    ],
    [[0, 0, 0]]

]

for index in range(len(inputs)):
    ret = Solution().threeSum(inputs[index])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]


print("All tests passed")
