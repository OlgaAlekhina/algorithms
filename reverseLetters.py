def reverse_letters(s: str) -> str:
    s_list = list(s)
    start, end = 0, len(s_list) - 1
    while start < end:
        if s_list[start].isalpha() and s_list[end].isalpha():
            s_list[start], s_list[end] = s_list[end], s_list[start]
            end -= 1
            start += 1
        elif s_list[start].isalpha():
            end -= 1
        elif s_list[end].isalpha():
            start += 1
        else:
            end -= 1
            start += 1

    return ''.join(s_list)


print(reverse_letters("a-bC-dEf-ghIj"))

# Given a string s, reverse the string according to the following rules:
#
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.
#
#
#
# Example 1:
#
# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:
#
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
#
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.