def longest_substring(s: str) -> int:
    xor_dict, xor_sum, res = {0: [-1]}, 0, 0
    vowels_dict = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
    for ind, val in enumerate(s):
        if val in vowels_dict:
            xor_sum ^= vowels_dict.get(val)
        if xor_sum in xor_dict:
            if len(xor_dict.get(xor_sum)) == 2:
                xor_dict[xor_sum][1] = ind
            else:
                xor_dict[xor_sum].append(ind)
        else:
            xor_dict[xor_sum] = [ind]
    for interval in xor_dict.values():
        if len(interval) == 2 and interval[1] - interval[0] > res:
            res = interval[1] - interval[0]

    return res


print(longest_substring("bcbcbc"))

# Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
#
#
#
# Example 1:
#
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
# Example 2:
#
# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
# Example 3:
#
# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
#
#
# Constraints:
#
# 1 <= s.length <= 5 x 10^5
# s contains only lowercase English letters.