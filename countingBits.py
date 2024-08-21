from typing import List


def counting_bits(n: int) -> List[int]:
    if n == 0:
        return [0]
    ans = [0, 1]
    while n > 1:
        len_ans = len(ans)
        mid = len_ans // 2
        while mid < len_ans:
            for i in range(mid, len_ans):
                ans.append(ans[i])
                n -= 1
                if n == 1:
                    return ans
            mid = (mid + len_ans) // 2 + 1 if mid % 2 > 0 else (mid + len_ans) // 2
        ans.append(ans[-1] + 1)
        n -= 1

    return ans


print(counting_bits(106))

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
#
#
#
# Example 1:
#
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:
#
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
#
# Constraints:
#
# 0 <= n <= 105
#
#
# Follow up:
#
# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?