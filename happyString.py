def happy_string(a: int, b: int, c: int) -> str:
    res = ''
    letters_list = sorted(list(zip((a, b, c), ('a', 'b', 'c'))), reverse=True)
    count1, count2, count3 = letters_list[0][0], letters_list[1][0], letters_list[2][0]
    max_pairs = count1 // 2 if count1 % 2 == 0 else count1 // 2 + 1
    if count2 + count3 <= max_pairs:
        while count1 > 0:
            res += letters_list[0][1] if count1 == 1 else letters_list[0][1] * 2
            count1 -= 2
            if count2:
                res += letters_list[1][1]
                count2 -= 1
            elif count3:
                res += letters_list[2][1]
                count3 -= 1
            else:
                break
    else:
        extra2 = count2 - max_pairs - 1
        extra3 = count3 - max_pairs - 1
        while count1 > 0:
            if count2:
                res += letters_list[1][1] if extra2 < 1 else letters_list[1][1] * 2
                count2 -= 1
                extra2 -= 1 if extra2 > 0 else 0
            if count3 and extra3 < 0:
                extra3 += 1
            elif count3 and extra3 >= 0:
                res += letters_list[2][1] if extra3 == 0 else letters_list[2][1] * 2
                count3 -= 1
                extra3 -= 1 if extra3 > 0 else 0
            res += letters_list[0][1] if count1 == 1 else letters_list[0][1] * 2
            count1 -= 2
        if count2:
            res += letters_list[1][1] if extra2 == 0 else letters_list[1][1] * 2
        if count3:
            res += letters_list[2][1] if extra3 == 0 else letters_list[2][1] * 2

    return res


print(happy_string(18, 7, 7))

# A string s is called happy if it satisfies the following conditions:
#
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
#
# A substring is a contiguous sequence of characters within a string.
#
#
#
# Example 1:
#
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# Example 2:
#
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.
#
#
# Constraints:
#
# 0 <= a, b, c <= 100
# a + b + c > 0