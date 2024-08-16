# brute force solution which got time exceed limits error on LeetCode

from typing import List


def num_teams(rating: List[int]) -> int:
    team_count, i = 0, 0
    while i < len(rating) - 2:
        j = i + 1
        while j < len(rating) - 1:
            k = j + 1
            while k < len(rating):
                if (rating[k] > rating[j] and rating[j] > rating[i]) or (rating[k] < rating[j] and rating[j] < rating[i]):
                    team_count += 1
                    print((rating[i], rating[j], rating[k]))
                k += 1
            j += 1
        i += 1

    return team_count


print(num_teams([21,200,33,14,5,1,6,15]))

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