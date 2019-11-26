from twosums.solution_1 import Solution

inputs = [
    [[2, 7, 11, 15], 9],
    [[4, 5, 3, 6], 8]
]

outputs =[
    [0, 1],
    [1, 2]
]

for index in range(len(inputs)):
    ret = Solution().twoSum(inputs[index][0], inputs[index][1])
    print(ret)
    assert ret == outputs[index]

print("All tests passed")
