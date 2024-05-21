def find_range(nums, target):
    nums_dict = {}
    for ind, num in enumerate(nums):
        for key in nums_dict:
            val = nums_dict.get(key) + num
            if val == target:
                return (key, ind + 1)
            nums_dict[key] = val
        nums_dict[ind] = num

        
print(find_range([1, -3, 2, 1, 4, 2, 8, -1], 9))



# Дан список интов и число-цель. Нужно найти такой range, чтобы сумма его элементов давала число-цель.
#
# elements = [1, -3, 4, 5]
#
# target = 9
#
# result = range(2, 4) # because elements[2] + elements[3] == target