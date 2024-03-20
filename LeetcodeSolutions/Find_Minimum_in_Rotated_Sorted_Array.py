def find_min_rotations(_list):
    low, high = 0, len(_list)-1
    while low<=high:
        mid_index = (low+high) // 2

        if _list[mid_index-1] > _list[mid_index]:
            return [mid_index, _list[mid_index]]
        elif _list[mid_index] > _list[high]:
            low = mid_index + 1
        else:
            high = mid_index - 1

list = [3,4,5,1,2]
list2 = [4,5,6,7,0,1,2]

print(find_min_rotations(list))
print(find_min_rotations(list2))


class Solution:
    def findMin(self, nums):
        if len(nums) == 1: return nums[0]
        low, high = 0, len(nums)-1
        while low<=high:
            mid_index = (low+high) // 2
            if nums[mid_index-1] > nums[mid_index]:
                return nums[mid_index]
            elif nums[mid_index] > nums[high]:
                low = mid_index + 1
            else:
                high = mid_index - 1
        return -1
    
s = Solution()
print(s.findMin(list2))
print(s.findMin(list))