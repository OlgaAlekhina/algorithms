def sub_interval(num_list):
    num_len = len(num_list)
    max_int, count_0, count_1, i = 0, 0, 0, 0
    while i < num_len:
        while i < num_len and num_list[i] != 1:
            i += 1
        if i == num_len and num_list[i - 1] == 0:
            break
        count_1 += 1
        i += 1
        while i < num_len:
            if num_list[i] == 1:
                count_1 += 1
            else:
                count_0 += 1
            if count_0 > 1:
                break
            i += 1
        if count_1 > max_int:
            max_int = count_1
        i += 1
        count_1, count_0 = 0, 0

    return max_int


print(sub_interval([1]))


# Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив ровно один элемент массива.

# [1, 1, 0]