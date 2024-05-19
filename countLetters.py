def count_letters(s):
    count = 1
    i = 0
    len_s = len(s)
    str_list = []
    while i < len_s:
        while i < len_s-1 and s[i+1] == s[i]:
            i += 1
            count += 1
        str_list.append(str(count)+s[i])
        count = 1
        i += 1
    return ''.join(str_list)


print(count_letters('aaabcccceefo'))