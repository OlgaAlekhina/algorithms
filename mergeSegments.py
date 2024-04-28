def merge_segments(segments):
    segments.sort()
    merge_seg = [segments[0]]
    for seg in segments:
        if merge_seg[-1][0] <= seg[0] < merge_seg[-1][1]:
            merge_seg[-1][1] = max(seg[1], merge_seg[-1][1])
        else:
            merge_seg.append(seg)
    return merge_seg


print(merge_segments([[1, 3], [100, 200], [2, 4]]))

# Например, имеем на входе:
#
# [1; 5]
# [2; 4]
# [7; 9]
# [3; 6]
# тогда, на выходе необходимо получить:
#
# [1; 6] // здесь слиты [1; 5], [2; 4], [3; 6]
# [7; 9]