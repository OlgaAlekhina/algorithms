def reverse_vowels(s: str) -> str:
    s_list = list(s)
    vowels = ('a', 'e', 'i', 'o', 'u')
    p1, p2 = 0, len(s) - 1
    while p1 < p2:
        flag1, flag2 = False, False
        while p1 < p2 and (not flag1 or not flag2):
            if s[p1].lower() in vowels:
                flag1 = True
            else:
                p1 += 1
            if s[p2].lower() in vowels:
                flag2 = True
            else:
                p2 -= 1
        if flag1 and flag2:
            s_list[p1], s_list[p2] = s_list[p2], s_list[p1]
        p1 += 1
        p2 -= 1

    return ''.join(s_list)


print(reverse_vowels('oluora'))

# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
#
#
# Example 1:
#
# Input: s = "hello"
# Output: "holle"
# Example 2:
#
# Input: s = "leetcode"
# Output: "leotcede"
#
#
# Constraints:
#
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.