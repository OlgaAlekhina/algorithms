def common_list(list1, list2):
    list1.sort()
    list2.sort()
    i, j = 0, 0
    common_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            common_list.append(list1[i])
            i += 1
            j += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            i += 1
    return common_list


print(common_list([1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2]))


# Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть [1, 2, 2, 3] (порядок неважен)