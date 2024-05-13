def similar_strings(st1, st2):
    l1, l2 = len(st1), len(st2)
    if l1 - l2 > 1 or l1 - l2 < 0:
        return False
    err_count = 0
    i, j = 0, 0
    while i < l1 and j < l2:
        if st1[i] == st2[j]:
            i += 1
            j += 1
        else:
            err_count += 1
            if err_count == 2:
                return False
            if l1 == l2:
                i += 1
                j += 1
            else:
                i += 1

    return True


print(similar_strings('abcdefg', 'abcdel'))