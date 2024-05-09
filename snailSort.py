def snail_sort(arr):
    sorted_arr = []
    i, j = 0, len(arr[0]) - 1
    while i <= j:
        for k in range(i, j + 1):
            sorted_arr.append(arr[i][k])
        for k in range(i + 1, j + 1):
            sorted_arr.append(arr[k][j])
        for k in range(j - 1, i - 1, -1):
            sorted_arr.append(arr[j][k])
        for k in range(j - 1, i, -1):
            sorted_arr.append(arr[k][i])
        i += 1
        j -= 1

    return sorted_arr


print(snail_sort([[1,2,3,4,5],[6,7,8,9,10],[1,2,3,4,5],[6,7,8,9,10],[1,2,3,4,5]]))



# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
#
# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].