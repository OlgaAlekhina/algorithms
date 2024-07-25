from typing import List


def sort_array(nums: List[int]) -> List[int]:

    def merge_lists(list1, list2):
        cur1, cur2 = 0, 0
        res_list = []
        while cur1 < len(list1) and cur2 < len(list2):
            if list1[cur1] <= list2[cur2]:
                res_list.append(list1[cur1])
                cur1 += 1
            else:
                res_list.append(list2[cur2])
                cur2 += 1
        if cur1 < len(list1):
            res_list.extend(list1[cur1:])
        elif cur2 < len(list2):
            res_list.extend(list2[cur2:])
        return res_list

    def help_func(arr, start, end):
        l = len(nums)
        if l == 1:
            return nums
        mid = l // 2
        return merge_lists(sort_array(nums[:mid]), sort_array(nums[mid:]))

    return help_func(nums, 0, len(nums) - 1)

        
print(sort_array([5,1,-5,100,-30,7,2,75,-99,1,2,0,0]))


# Given an array of integers nums, sort the array in ascending order and return it.
#
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
#
#
#
# Example 1:
#
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:
#
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104