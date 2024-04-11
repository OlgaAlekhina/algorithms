def convert_list(num_list):
    new_list = []
    num_list.sort()
    i = 0
    while i < len(num_list) - 1:
        if num_list[i + 1] - num_list[i] != 1:
            new_list.append(str(num_list[i]))
            i += 1
        else:
            num_range = str(num_list[i]) + '-'
            while i < len(num_list) - 1 and num_list[i + 1] - num_list[i] == 1:
                i += 1
            num_range += str(num_list[i])
            new_list.append(num_range)
            i += 1
    if i == len(num_list) - 1:
        new_list.append(str(num_list[-1]))
    return ','.join(new_list)
    
    
print(convert_list([1,4,5,2,3,9,8,11,10]))
        

# Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"