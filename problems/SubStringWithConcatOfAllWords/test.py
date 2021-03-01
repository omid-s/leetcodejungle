from problems.SubStringWithConcatOfAllWords.solution_1 import Solution
from classes.Tools import array_equal

inputs = [
    ["barfoothefoobarman", ["foo", "bar"]],
    ["wordgoodgoodgoodbestword", ["word", "good", "best", "word"]],
    ["barfoofoobarthefoobarman", ["bar", "foo", "the"]]
]
outputs = [
    [0, 9],
    [],
    [6, 9, 12]

]

for index in range(len(inputs)):
    ret = Solution().fidnSubstring(inputs[index][0],inputs[index][1])
    print(outputs[index], "-->", ret)
    assert array_equal(ret, outputs[index])

print("All tests passed")
