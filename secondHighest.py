def second_highest(s: str) -> int:
    nums_set = set()
    for char in s:
        if char.isdigit():
            nums_set.add(int(char))
    if len(nums_set) < 2:
        return -1
    nums_set.remove(max(nums_set))

    return max(nums_set)


print(second_highest("ck077"))

# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
#
# An alphanumeric string is a string consisting of lowercase English letters and digits.
#
#
#
# Example 1:
#
# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
# Example 2:
#
# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest digit.
#
#
# Constraints:
#
# 1 <= s.length <= 500
# s consists of only lowercase English letters and digits.