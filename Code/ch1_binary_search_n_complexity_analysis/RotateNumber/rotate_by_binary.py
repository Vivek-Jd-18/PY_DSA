# get numbers of rotations by binary search method

def rotations_by_binary(_list):
    low, high = 0, len(_list)-1
    while(low<=high):
        mid_index = (low + high) // 2

        if _list[mid_index-1] > _list[mid_index]:
            return mid_index
        elif _list[high] < _list[mid_index]:
            low = mid_index + 1
        else:
            high = mid_index - 1
    return 0

l1 = [5,6,7,1,2,3,4]
print(rotations_by_binary(l1) == 3)
l1 = [4,5,6,7,8,1,2]
print(rotations_by_binary(l1) == 5)
l1 = [5,6,1,2,3,4]
print(rotations_by_binary(l1) == 2)