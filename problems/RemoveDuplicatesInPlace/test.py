from problems.RemoveDuplicatesInPlace.solution_1 import Solution

inputs = [
    [1, 2, 3],
    [1, 1, 2, 3],
    [0, 0, 0, 1, 1, 1, 1, 1, 3, 4, 5, 5],
    [0, 0, 0]
]

outputs = [
    [3, [1, 2, 3]],
    [3, [1, 2, 3]],
    [5, [0, 1, 3, 4, 5]],
    [1, [0]]
]


def verify_n_first(n, y, y_hat):
    for i in range(n):
        if y[i] != y_hat[i]:
            return False
    return True


for index in range(len(inputs)):
    ret = Solution().removeDuplicates(inputs[index])
    print(outputs[index], "-->", ret, inputs[index])
    assert ret == outputs[index][0] and verify_n_first(ret, outputs[index][1], inputs[index])

print("All tests passed")
