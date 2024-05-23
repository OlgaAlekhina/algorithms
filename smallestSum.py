def smallest_sum(nums):
    min_num = min(nums)
    divs = [d for d in range(1, min_num // 2 + 1) if min_num % d == 0] + [min_num]
    for num in nums:
        if len(divs) == 1:
            return len(nums)
        while len(divs) > 1:
            if num % divs[-1] == 0:
                break
            else:
                divs.pop()
        
    return divs[-1] * len(nums)


print(smallest_sum([1834616, 78750, 358400, 2251214, 2411150, 2075150, 1105454, 463736, 1451576, 1310904, 813134, 2140334, 172494, 659246, 2085944, 1561784, 1345400, 68600, 1362816, 2173304, 39326, 2685816, 270494, 310814, 64736, 266616, 510734, 64736, 1035776, 2376416, 1656704, 582624, 286286, 665336, 510734, 315000, 255150, 332024, 2552606, 1764350, 500094, 753536, 3402686, 500094, 453600, 1589966, 1380344, 1406846, 1302350, 57344, 819896, 2118494, 148526, 270494, 2010974, 240254, 702464, 3105774, 278334, 371966, 2364894, 1362816, 105966, 2032254, 163296, 1328096, 1058750, 3402686, 123704, 1251614, 87374, 2923886, 2588600, 45486, 1666350, 1580544, 2872926, 47096, 521486, 1354094, 734174, 3172064, 178766, 2195424, 2936696, 3306744, 1097600, 793016, 345086, 166334, 500094, 286286]))

# Given an array X of positive integers, its elements are to be transformed by running the following operation on them as many times as required:
#
# if X[i] > X[j] then X[i] = X[i] - X[j]
#
# When no more transformations are possible, return its sum ("smallest possible sum").
#
# For instance, the successive transformation of the elements of input X = [6, 9, 21] is detailed below:
#
# X_1 = [6, 9, 12] # -> X_1[2] = X[2] - X[1] = 21 - 9
# X_2 = [6, 9, 6]  # -> X_2[2] = X_1[2] - X_1[0] = 12 - 6
# X_3 = [6, 3, 6]  # -> X_3[1] = X_2[1] - X_2[0] = 9 - 6
# X_4 = [6, 3, 3]  # -> X_4[2] = X_3[2] - X_3[1] = 6 - 3
# X_5 = [3, 3, 3]  # -> X_5[1] = X_4[0] - X_4[1] = 6 - 3
# The returning output is the sum of the final transformation (here 9).
#
# Example
# solution([6, 9, 21]) #-> 9
# Solution steps:
# [6, 9, 12] #-> X[2] = 21 - 9
# [6, 9, 6] #-> X[2] = 12 - 6
# [6, 3, 6] #-> X[1] = 9 - 6
# [6, 3, 3] #-> X[2] = 6 - 3
# [3, 3, 3] #-> X[1] = 6 - 3
# Additional notes:
# There are performance tests consisted of very big numbers and arrays of size at least 30000. Please write an efficient algorithm to prevent timeout.