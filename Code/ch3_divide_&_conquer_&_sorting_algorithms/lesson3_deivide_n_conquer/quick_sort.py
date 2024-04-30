# Quick-Sort (Divide n Conquer)

# def quick_sort(list, pivot)->list[int]:
#     pass

def quicksort(arr):  
    if len(arr) < 2:  
        return arr  
    pivot = arr[0]  
    left = [x for x in arr[1:] if x < pivot]  
    right = [x for x in arr[1:] if x >= pivot]  
    return quicksort(left) + [pivot] + quicksort(right)  

print(quicksort([3, 5, 7, 2, 4, 6, 8]),"res")

#  3, 5, 7, 2, 4, 6, '8'
#  ['3', 5, 7, 2, 4, 6, 8] []    
#  [2] '3' [5, 7, 4, 6, 8]
#   2 , 3 , 
# 
# 
# 
# 
# 
# 
