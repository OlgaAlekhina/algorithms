def remove_occurrences(s: str, part: str) -> str:
    res, ind_list, part_len, i = '', [], len(part), 0
    while i < len(s):
        if s[i] == part[0]:
            if s[i:i+part_len] == part:
                i += part_len
                for ind in ind_list[::-1]:
                    last_len = len(res) - ind
                    if (res[ind:] + s[i:i+part_len-last_len]) == part:
                        res = res[:ind]
                        i += part_len-last_len
                        del(ind_list[ind:])
            else:
                ind_list.append(len(res))
                res += s[i]
                i += 1
        else:
            res += s[i]
            i += 1

    return res


print(remove_occurrences(s = "avtjogzavshnomyochrrwtxedldenqyszxejcgqoksmyzgfifjiwrzimsgcyoqcultmxvolfhwcsjipjlvaceeoxavtjogzavshnomyochrrwtxedldenqyszxejcgqoksmyzgfifjiwrzimsgcyoqcultmxvolfhwcsjipjlvaceeoxexaehmmneivlscizwzqckdqusbhwosqitxbkgtvhfjpzchwwuvflpdlksldqigioembrrekuwamhhvkrakrhlbbnhjtvcxjmpygnvszgwvjxrszawpwhyuykbzyyeecscusbvdcjolammskjhalzcozqpdobzmmggrefyyzgxqnrdxwzswlboynqbgbiwyyiukqnqnmmvjfpacmwmwxaacuejcwjjocotacgkgtahsrsqgqknwukyolxhaaezivyezpjabsdkhdthqmbwqwjdablqkcxpxwgjwdtzmgqyhjhmfukhzmqdzebbwbsjyvbstijoraxbicpkuehjkqjhxlexaehmmneivlscizwzqckdqusbhwosqitxbkgtvhfjpzchwwuvflpdlksldqigioembrrekuwamhhvkrakrhlbbnhjtvcxjmpygnvszgwvjxrszawpwhyuykbzyyeecscusbvdcjolammskjhalzcozqpdobzmmggrefyyzgxqnrdxwzswlboynqbgbiwyyiukqnqnmmvjfpacmwmwxaacuejcwjjocotacgkgtahsrsqgqknwukyolxhaaezivyezpjabsdkhdthqmbwqwjdablqkcxpxwgjwdtzmgqyhjhmfukhzmqdzebbwbsjyvbstijoraxbicpkuehjkqjhxlepgnzrlbzytiaasnnahnbjiqgwiossjxsowggbguovdikhqrdcpheamfysdjgvykvxhqxyxmnylkftkqstpqbspuoyckpkvttagylycvpxgdbaemzhbgjmlkcccaniibqetjy", part = "avtjogzavshnomyochrrwtxedldenqyszxejcgqoksmyzgfifjiwrzimsgcyoqcultmxvolfhwcsjipjlvaceeoxexaehmmneivlscizwzqckdqusbhwosqitxbkgtvhfjpzchwwuvflpdlksldqigioembrrekuwamhhvkrakrhlbbnhjtvcxjmpygnvszgwvjxrszawpwhyuykbzyyeecscusbvdcjolammskjhalzcozqpdobzmmggrefyyzgxqnrdxwzswlboynqbgbiwyyiukqnqnmmvjfpacmwmwxaacuejcwjjocotacgkgtahsrsqgqknwukyolxhaaezivyezpjabsdkhdthqmbwqwjdablqkcxpxwgjwdtzmgqyhjhmfukhzmqdzebbwbsjyvbstijoraxbicpkuehjkqjhxl"))

# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/?envType=daily-question&envId=2025-02-11
# Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
#
# Find the leftmost occurrence of the substring part and remove it from s.
# Return s after removing all occurrences of part.
#
# A substring is a contiguous sequence of characters in a string.
#
#
#
# Example 1:
#
# Input: s = "daabcbaabcbc", part = "abc"
# Output: "dab"
# Explanation: The following operations are done:
# - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
# - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
# - s = "dababc", remove "abc" starting at index 3, so s = "dab".
# Now s has no occurrences of "abc".
# Example 2:
#
# Input: s = "axxxxyyyyb", part = "xy"
# Output: "ab"
# Explanation: The following operations are done:
# - s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
# - s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
# - s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
# - s = "axyb", remove "xy" starting at index 1 so s = "ab".
# Now s has no occurrences of "xy".
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# 1 <= part.length <= 1000
# s​​​​​​ and part consists of lowercase English letters.