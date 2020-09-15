from problems.MergeTwoSortedLists.solution_1 import Solution
from classes.Tools import str2LinkedList
from classes.Tools import *

inputs = [
    ["1->3->5", "2->4"],
    ["1->2->3", "4->5"],
    ["1", "2->3->4->5"],
    ["1->2", "1"]

]
outputs = [
    "1->2->3->4->5",
    "1->2->3->4->5",
    "1->2->3->4->5",
    "1->1->2"
]

for index in range(len(inputs)):
    ret = Solution().mergeTwoLists(str2LinkedList(inputs[index][0]), str2LinkedList(inputs[index][1]))
    print(outputs[index], " --> ", linkedlist2Str(ret))
    assert linkedlist2Str(ret) == outputs[index]

print("All tests passed")
