from typing import List


def min_time_difference(time_points: List[str]) -> int:
    if len(set(time_points)) < len(time_points):
        return 0
    time_points.sort()
    time0 = sum(a * b for a, b in zip(map(int, time_points[0].split(':')), [60, 1]))
    time1 = sum(a * b for a, b in zip(map(int, time_points[1].split(':')), [60, 1]))
    res = time1 - time0
    for i in range(2, len(time_points)):
        time2 = sum(a * b for a, b in zip(map(int, time_points[i].split(':')), [60, 1]))
        res = min(time2 - time1, res)
        time1 = time2
    res = min(1440 - time1 + time0, res)

    return res


print(min_time_difference(["00:00","23:59","07:57"]))

# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
#
#
# Example 1:
#
# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Example 2:
#
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
#
#
# Constraints:
#
# 2 <= timePoints.length <= 2 * 104
# timePoints[i] is in the format "HH:MM".