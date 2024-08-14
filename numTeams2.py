from typing import List


def num_teams(rating: List[int]) -> int:
    team_count = 0
    for i in range(1, len(rating) - 1):
        count_s, count_l = 0, 0
        for j in range(i):
            if rating[j] < rating[i]:
                count_s += 1
            elif rating[j] > rating[i]:
                count_l += 1
        for k in range(i + 1, len(rating)):
            if rating[k] > rating[i]:
                team_count += count_s
            elif rating[k] < rating[i]:
                team_count += count_l

    return team_count


print(num_teams([21,200,330]))

# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
#
# You have to form a team of 3 soldiers amongst them under the following rules:
#
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
#
#
#
# Example 1:
#
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
# Example 2:
#
# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
# Example 3:
#
# Input: rating = [1,2,3,4]
# Output: 4
#
#
# Constraints:
#
# n == rating.length
# 3 <= n <= 1000
# 1 <= rating[i] <= 105
# All the integers in rating are unique.