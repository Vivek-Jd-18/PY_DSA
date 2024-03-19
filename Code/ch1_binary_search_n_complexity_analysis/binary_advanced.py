from jovian.pythondsa import evaluate_test_case

# this approach finds an index of target element, in case there are duplicate target
# elements it will return first occurance of target

def filter_duplicates(_list,_target,_mid_index, _mid_value):
    if _mid_value == _target:
        if _mid_index-1 >=0 and _list[_mid_index-1] == _target:
            return 'left'
        else: 
            return 'found'
    elif _mid_value < _target:
        return 'right'
    else:
        return 'left'

def binary_ad(_list,_target):
    low, high = 0, len(_list) - 1
    
    while low<= high:
        mid_index = (low + high) // 2
        mid_value = _list[mid_index]

        result = filter_duplicates(_list,_target,mid_index,mid_value)

        if result == 'found':
            return mid_index
        elif result == 'left':
            high = mid_index - 1
        elif result == 'right':
            low = mid_index + 1

        # if mid_value == _target:
        #     return mid_index
        # elif mid_value < _target:
        #     low = mid_index + 1
        # elif mid_value > _target:
        #     high = mid_index -1
    return -1

test1 = {"input":{"_list":[1,2,3,4],"_target":2},"output":1}
test2 = {"input":{"_list":[11,23,34,45,67,89,90],"_target":89},"output":5}
test3 = {"input":{"_list":[1,2,3,4],"_target":2},"output":1}
test4 = {"input":{"_list":[1,2,3,4,4,4,4,5,6,6,6,7,8,9],"_target":4},"output":3}

evaluate_test_case(binary_ad,test1)
evaluate_test_case(binary_ad,test2)
evaluate_test_case(binary_ad,test3)
evaluate_test_case(binary_ad,test4)