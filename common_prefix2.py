def longest_common_prefix(strs):
    len_strs = len(strs)
    if len_strs == 1:
        return strs[0]
    min_l = min(map(lambda x: len(x), strs))
    if min_l == 0:
        return ''
    pref = ''
    for i in range(min_l):
        for j in range(1, len_strs):
            if strs[0][i] != strs[j][i]:
                return pref
        pref = strs[0][:i+1]

    return pref
                
        
print(longest_common_prefix(["flower","flow","flight"]))

# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.