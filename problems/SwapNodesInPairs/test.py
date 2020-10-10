from problems.SwapNodesInPairs.solution_1 import Solution
from classes.Tools import str2LinkedList
from classes.Tools import *

inputs = [
    ["1->3->5"],
    ["1->2->3->4->5"],
    ["2->3->4->5"],
    ["1->2"],
    ["1"]

]
outputs = [
    "3->1->5",
    "2->1->4->3->5",
    "3->2->5->4",
    "2->1",
    "1"
]

for index in range(len(inputs)):
    ret = Solution().swapPairs(str2LinkedList(inputs[index][0]))
    print(outputs[index], " --> ", linkedlist2Str(ret))
    assert linkedlist2Str(ret) == outputs[index]

print("All tests passed")
