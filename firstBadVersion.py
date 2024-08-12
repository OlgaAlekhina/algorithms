# The isBadVersion API is already defined for you.
def is_bad_version(version: int) -> bool:
    bad_version = 4
    if version >= bad_version:
        return True
    return False


def first_bad_version(n: int) -> bool:
    def bin_search(start, end, flag):
        if start == end:
            if flag:
                if is_bad_version(start):
                    return start
                return start + 1
            else:
                return start
        mid = (end + start) // 2
        if is_bad_version(mid):
            return bin_search(start, mid, True)
        else:
            return bin_search(mid + 1, end, False)

    return bin_search(1, n, False)


print(first_bad_version(4))

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
#
#
#
# Example 1:
#
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:
#
# Input: n = 1, bad = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= bad <= n <= 231 - 1