from collections import defaultdict


def common_list(list1, list2):
    common_list = []
    d1 = defaultdict(int)
    for k in list1:
        d1[k] += 1
    for num in list2:
        if num in d1 and d1.get(num) > 0:
            common_list.append(num)
            d1[num] = d1.get(num) - 1
    return common_list


print(common_list([1, 2, 3, 2, 0, 5], [5, 1, 2, 7, 3, 2]))


# Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть [1, 2, 2, 3] (порядок неважен)