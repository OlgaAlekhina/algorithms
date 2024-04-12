def search_insert(nums, target):
    f_index = 0
    l_index = len(nums) - 1
    return binary_search(nums, f_index, l_index, target)


def binary_search(num_list, f_index, l_index, value):
    if l_index > f_index:
        mid_index = (f_index + l_index) // 2
        mid_elem = num_list[mid_index]
        if value == mid_elem:
            return mid_index
        elif value < mid_elem:
            l_index = mid_index - 1
            return binary_search(num_list, f_index, l_index, value)
        elif value > mid_elem:
            f_index = mid_index + 1
            return binary_search(num_list, f_index, l_index, value)
    if value == num_list[f_index]:
        return f_index
    elif value > num_list[f_index]:
        return f_index + 1
    else:
        return f_index


print(search_insert([2, 3, 5, 10, 12, 20, 33, 71, 111, 230], 111))







