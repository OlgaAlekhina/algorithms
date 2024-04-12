def binary_search(num_list, f_index, l_index, value):
    if l_index >= f_index:
        mid_index = (f_index + l_index) // 2
        mid_elem = num_list[mid_index]
        if value == mid_elem:
            return mid_index
        elif value < mid_elem:
            l_index2 = mid_index - 1
            return binary_search(num_list, f_index, l_index2, value)
        elif value > mid_elem:
            f_index2 = mid_index + 1
            return binary_search(num_list, f_index2, l_index, value)
    return "no match"


print(binary_search([2, 3, 5, 10, 12, 20, 33, 71, 111, 230], 0, 9, 230))







