def longest_common_prefix(strs):
    pref = ''
    if len(strs) == 1:
        pref = strs[0]
    min_l = len(strs[0])
    for i in range(1, len(strs)):
        if len(strs[i]) <= min_l:
            min_l = len(strs[i])
    if min_l == 0:
        pref = ''
    else:
        for i in range(min_l):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    pref = strs[0][:i]
                    break
                else:
                    pref = strs[0][:i+1]
            else:
                continue
            break
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
# Explanation: There is no common prefix among the input strings.