from problems.ZigZagConversion.solution_1 import Solution

inputs = [
    ["PAYPALISHIRING", 3],
    ["PAYPALISHIRING", 4],
    ["PAYPALISHIRING", 14],
    ["PAYPALISHIRING", 18]
]

outputs = [
    "PAHNAPLSIIGYIR",
    "PINALSIGYAHRPI",
    "PAYPALISHIRING",
    "PAYPALISHIRING"
]

for index in range(len(inputs)):
    ret = Solution().convert(inputs[index][0], inputs[index][1])
    print(outputs[index], "-->", ret)
    assert ret == outputs[index]

print("All tests passed")
