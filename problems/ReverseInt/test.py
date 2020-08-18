from problems.ReverseInt.solution_2 import Solution

inputs = [
    123,
    -322,
    120,
    1111111111111111999999999999999999,
    -120
]

outputs = [
    321,
    -223,
    21,
    0,
    -21
]

for index in range(len(inputs)):
    ret = Solution().reverse(inputs[index])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]

print("All tests passed")
