# merge short

def merge_short(list)->list[int]:
    l = len(list)
    if l <= 1:
        return list
    mid = l // 2
    left = list[:mid]
    right = list[mid:]
    left_list, right_list = merge_short(left), merge_short(right)
    return merge(left_list, right_list)

def merge(left_list, right_list)->list[int]:
    li = []
    i,j = 0,0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            li.append(left_list[i])
            i+=1
        else:
            li.append(right_list[j])
            j+=1
    left, right = left_list[i:], right_list[j:]
    return li + left + right

l = [2,4,6,8,1,3,7]

print(merge_short(l))