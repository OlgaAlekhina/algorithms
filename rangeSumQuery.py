class NumArray:

    def __init__(self, nums):
        self.nums = nums
        len_list = len(self.nums)
        pref_sum = [0] * (len_list + 1)
        self.pref_sum = pref_sum
        for i in range(1, len_list + 1):
            pref_sum[i] = pref_sum[i - 1] + self.nums[i - 1]

        
    def sum_range(self, left: int, right: int) -> int:
        return self.pref_sum[right + 1] - self.pref_sum[left]


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sum_range(2, 5))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# [0, -2, -2, 1, -4, -2, -3]

# Given an integer array nums, handle multiple queries of the following type:
#
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
#
#
# Example 1:
#
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
#
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= left <= right < nums.length
# At most 104 calls will be made to sumRange.