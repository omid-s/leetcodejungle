from problems.ReverseNodesInKGroup.solution_1 import Solution
from classes.Tools import str2LinkedList
from classes.Tools import *

inputs = [
    ["1->3->5", 2],
    ["1->2->3->4->5", 3],
    ["2->3->4->5", 1],
    ["1->2", 2],
    ["1", 1],
    ["", 1],
    ["1->2->3->4->5", 2]
]
outputs = [
    "3->1->5",
    "3->2->1->4->5",
    "2->3->4->5",
    "2->1",
    "1",
    "",
    "2->1->4->3->5"
]

for index in range(len(inputs)):
    ret = Solution().reverseKGroup(str2LinkedList(inputs[index][0]),inputs[index][1])
    print(outputs[index], " --> ", linkedlist2Str(ret))
    assert linkedlist2Str(ret) == outputs[index]

print("All tests passed")
