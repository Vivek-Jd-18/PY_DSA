# merge short
def merge(left_list, right_list, depth=0) -> list[int]:
    print(' '*depth, 'merge', left_list, right_list)
    i, j, li = 0, 0, []
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            li.append(left_list[i])
            i += 1
        else:
            li.append(right_list[j])
            j += 1
    return li + left_list[i:]+ right_list[j:]

def merge_short(list, depth = 0) -> list[int]:
    print(' '*depth, 'merge_sort', list)
    if len(list) < 2:
        return list
    mid = len(list) // 2
    return merge(merge_short(list[:mid],depth+1), merge_short(list[mid:],depth+1),depth+1)

l = [4, 1, 3, 9, 7]
# merge_short(l)
print(merge_short(l))




# [1, 4, 7] [0, 2, 3] => [ ?, ?, ?, ?, ?, ? ]
# [1, 4, 7] [0, 2, 3] => [ 0, ?, ?, ?, ?, ? ]
# [1, 4, 7] [0, 2, 3] => [ 0, 1, ?, ?, ?, ? ]
# [1, 4, 7] [0, 2, 3] => [ 0, 1, 2, ?, ?, ? ]
# [1, 4, 7] [0, 2, 3] => [ 0, 1, 3, ?, ? ]
# [1, 4, 7] [0, 2, 3] => [ 0, 1, 2, 3, 4, ? ]
# [1, 4, 7] [0, 2, 3] => [ 0, 1, 2, 3, 4, 7 ]
# [1, 4, 7] [0, 2, 3] => [ 0, 1, 2, 3, 4, 7 ]

# one recursion(log n) and a while loop(n) => O(n log n)