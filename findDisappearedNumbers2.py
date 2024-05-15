def find_disappeared_numbers(nums):
    arr = []
    i = 0
    while i < len(nums):
        if nums[i] == i + 1 or nums[i] == nums[nums[i] - 1]:
            i += 1
            continue
        else:
            j = nums[i]
            while True:
                x = nums[j - 1]
                nums[j - 1] = j
                if nums[x - 1] != x:
                    j = x
                else:
                    break               
        i += 1
    for ind, val in enumerate(nums):
        if val != ind + 1:
            arr.append(ind + 1)
            
    return arr
        

print(find_disappeared_numbers([5,3,2,3,3,5,1,3,4,8]))


# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
#
#
#
# Example 1:
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
#
# Input: nums = [1,1]
# Output: [2]
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
#
#
# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.