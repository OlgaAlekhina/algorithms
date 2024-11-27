def remove_letters(s: str) -> str:
    char_list = [0] * 26
    for char in s:
        char_list[ord(char) - ord('a')] += 1
    res = []
    for char in s:
        if char not in res:
            res.append(char)
        elif char in res and char != res[-1]:
            ind = res.index(char)
            if char > res[ind + 1]:
                res.pop(ind)
                res.append(char)
            else:
                single = False
                for i in range(ind+1, len(res)):
                    if char < res[i] and char_list[ord(res[i]) - ord('a')] == 0:
                        single = True
                    elif char > res[i] and single:
                        break
                    elif char > res[i] and not single:
                        res.pop(ind)
                        res.append(char)
                        break
        char_list[ord(char) - ord('a')] -= 1

    return ''.join(res)


print(remove_letters("cbccshkbbabdbacvnbdbueacdcbc"))

# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
# the smallest in lexicographical order
#  among all possible results.
#
#
#
# Example 1:
#
# Input: s = "bcabc"
# Output: "abc"
# Example 2:
#
# Input: s = "cbacdcbc"
# Output: "acdb"
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of lowercase English letters.