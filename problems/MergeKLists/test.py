from problems.MergeKLists.solution_1 import Solution
from classes.Tools import str2LinkedList
from classes.Tools import *

inputs = [
    ["1->4->5","1->3->4","2->6"],
    ["1", "2->3->4->5"],
    ["1->2", "1"],
    ["1", ""]

]
outputs = [
    "1->1->2->3->4->4->5->6",
    "1->2->3->4->5",
    "1->1->2",
    "1"
]

for index in range(len(inputs)):
    ret = Solution().mergeKLists([str2LinkedList(x) for x in inputs[index]])
    print(outputs[index], " --> ", linkedlist2Str(ret))
    assert linkedlist2Str(ret) == outputs[index]

print("All tests passed")
