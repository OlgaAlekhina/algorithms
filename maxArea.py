def max_area(height) -> int:
    l = len(height)
    max_cont = 0
    cur1, cur2 = 0, l - 1
    while cur1 < cur2:
        cont = min(height[cur1], height[cur2]) * (l - 1)
        if cont > max_cont:
            max_cont = cont
        if height[cur1] < height[cur2]:
            cur1 += 1
        else:
            cur2 -= 1
        l -= 1

    return max_cont


print(max_area([1,2,4,3]))


# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1
#
#
# Constraints:
#
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104