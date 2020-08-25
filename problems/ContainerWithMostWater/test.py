from problems.ContainerWithMostWater.solution_1 import Solution

inputs = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [1,3,40,50,2,12]
]

outputs = [
    49,
    40
]

for index in range(len(inputs)):
    ret = Solution().maxArea(inputs[index])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]


print("All tests passed")
