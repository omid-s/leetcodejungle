from problems.MedianofTwoSortedArrays.solution_1 import Solution

inputs = [
    [[1, 3], [2]],
    [[1, 2], [3, 4]],
    [[1, 3, 9], [4, 5, 10]],
    [[1, 2, 3], []],
    [[3, 6, 9, 10, 21], [2]],
    [[3], []]
]

outputs = [
    2.0,
    2.5,
    4.5,
    2.0,
    7.5,
    3.0
]

for index in range(len(inputs)):
    nums1 = inputs[index][0]
    nums2 = inputs[index][1]

    ret = Solution().findMedianSortedArrays(nums1, nums2)

    print("%s , %s : %f -> %f" % (str(nums1), str(nums2), outputs[index], ret))

    assert ret == outputs[index]

print("All tests passed")
