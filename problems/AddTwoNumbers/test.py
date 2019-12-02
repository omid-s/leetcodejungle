from problems.AddTwoNumbers.solution_1 import Solution
from classes.Tools import linked_list_to_list
from classes.Tools import print_linked_list
from classes.Tools import list_to_linked_list

inputs = [
    [[2, 7, 1, 1], [2, 2, 1]],
    [[4, 5, 3, 6], [4, 5, 3, 6]]
]

outputs = [
    [4, 9, 2, 1],
    [8, 0, 7, 2, 1]
]

for index in range(len(inputs)):
    l1 = list_to_linked_list(inputs[index][0])
    l2 = list_to_linked_list(inputs[index][1])

    print_linked_list(l1)
    print_linked_list(l2)
    ret = linked_list_to_list(Solution().addTwoNumbers(l1, l2))
    print(outputs[index], "-->", ret)
    print("----------------------")
    assert ret == outputs[index]

print("All tests passed")
