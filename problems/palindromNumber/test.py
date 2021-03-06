from problems.palindromNumber.solution_3 import Solution

inputs = [
    123,
    -322,
    121,
    112211,
    23432,
    949
]

outputs = [
    False,
    False,
    True,
    True,
    True,
    True
]

for index in range(len(inputs)):
    ret = Solution().isPalindrome(inputs[index])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]

print("All tests passed")