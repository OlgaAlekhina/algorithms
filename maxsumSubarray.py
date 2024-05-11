def maxsum_subarray(arr):
    max_sum = 0
    cur_sum = 0
    for num in arr:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)

    return max_sum if max_sum > 0 else 0


print(maxsum_subarray([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))

# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.