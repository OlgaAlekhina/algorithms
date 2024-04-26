def sum_int(nums):
    a, b = nums[0], nums[1]
    for i in range(2, len(nums)):
        if nums[i] < max(a, b):
            if a > b:
                a = nums[i]
            else:
                b = nums[i]

    return a + b


print(sum_int([1,6,3,4,5,9,2]))





# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
#
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
#
# [10, 343445353, 3453445, 3453545353453] should return 3453455.