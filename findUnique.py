def find_unique(nums):
    if nums[0] == nums[1]:
        double = nums[0]
    else:
        return nums[0] if nums[2] == nums[1] else nums[1]
    for num in nums:
        if num != double:
            return num



print(find_unique([ 1, 5, 5 ]))


# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.