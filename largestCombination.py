from typing import List


def largest_combination(candidates: List[int]) -> int:
    bits_list = [0] * 24
    for num in candidates:
        count = 0
        while num:
            if num & 1 == 1:
                bits_list[count] += 1
            num >>= 1
            count += 1

    return max(bits_list)


print(largest_combination([44,14,69,36,46,38,57,90,4,16,19,49,73,51,68,4,14,14,87,13,12,81,64,56,61,13,43,11,87,46,1,94,83,83,77,77,73,42,72,98,25,52,40,75,31,37,35,26,6,29,89,40,66,32,56,61,50,93,22,64,73,77,3,77,70,7,53,23,45,49,29,34]))

# The bitwise AND of an array nums is the bitwise AND of all integers in nums.
#
# For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
# Also, for nums = [7], the bitwise AND is 7.
# You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.
#
# Return the size of the largest combination of candidates with a bitwise AND greater than 0.
#
#
#
# Example 1:
#
# Input: candidates = [16,17,71,62,12,24,14]
# Output: 4
# Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
# The size of the combination is 4.
# It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
# Note that more than one combination may have the largest size.
# For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.
# Example 2:
#
# Input: candidates = [8,8]
# Output: 2
# Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
# The size of the combination is 2, so we return 2.
#
#
# Constraints:
#
# 1 <= candidates.length <= 105
# 1 <= candidates[i] <= 107