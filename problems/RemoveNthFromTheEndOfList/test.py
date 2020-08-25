from problems.RemoveNthFromTheEndOfList.solution_1 import Solution
from classes.Tools import str2LinkedList
from classes.Tools import *

inputs = [
    ["1->2->3->4->5", 2],
    ["1->2->3", 3]
]
outputs = [
    "1->2->3->5",
    "2->3"
]

for index in range(len(inputs)):
    ret = Solution().removeNthFromEnd(str2LinkedList(inputs[index][0]), inputs[index][1])
    print(outputs[index], " --> ", linkedlist2Str(ret))
    assert linkedlist2Str(ret) == linkedlist2Str(outputs[index])

print("All tests passed")
