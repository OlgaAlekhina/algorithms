from typing import List


def domino_pairs(dominoes: List[List[int]]) -> int:
    pairs_dict, res = {}, 0
    for pair in dominoes:
        pair1, pair2 = (pair[0], pair[1]), (pair[1], pair[0])
        if pair1 in pairs_dict:
            res += pairs_dict[pair1]
            pairs_dict[pair1] += 1
        elif pair2 in pairs_dict:
            res += pairs_dict[pair2]
            pairs_dict[pair2] += 1
        else:
            pairs_dict[pair1] = 1

    return res


print(domino_pairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))

# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
#
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
#
#
#
# Example 1:
#
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Example 2:
#
# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3
#
#
# Constraints:
#
# 1 <= dominoes.length <= 4 * 104
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9