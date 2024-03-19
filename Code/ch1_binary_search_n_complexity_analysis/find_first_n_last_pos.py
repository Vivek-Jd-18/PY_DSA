# programs shows use of binary search to get index of 
# first and last occurance of an elemnt from a list

from jovian.pythondsa import evaluate_test_case

def generic_binary_logic(_low, _high, _condition):
    while _low<=_high:
        # print(_low , _high)
        mid = (_low + _high) // 2
        res = _condition(mid)

        if res == 'found':
            return mid
        elif res == 'left':
            _high = mid - 1
        else:
            _low = mid +1
    return -1

def get_first_index(_list, _target):
    def condition(mid):
        if _list[mid] == _target:
            if _list[mid-1] == _target and mid >= 0:
                return 'left'
            else:
                return 'found'
        elif _list[mid] < _target:
            return 'right'
        else:
            return 'left'
    return generic_binary_logic(0, len(_list)-1, condition)

def get_last_index(_list, _target):
    def condition(mid):
        if _list[mid] == _target:
            if mid+1 < len(_list) -1 and _list[mid+1] == _target:
                return 'right'
            else:
                return 'found'
        elif _list[mid] > _target:
            return 'left'
        else:
            return 'right'
    
    return generic_binary_logic(0, len(_list)-1, condition)


# test0 = [1,2,3,4,5,6,6,6,6,6,7,8,9,10]
# print("first index {} and last index {} ".format(get_first_index(test0,6), get_last_index(test0,6)))

test1_first_occurance = {"input":{"_list":[1,2,3,3,3,3,4,5,6,7],"_target":3},"output":2}
test1_last_occurance =  {"input":{"_list":[1,2,3,3,3,3,4,5,6,7],"_target":3},"output":5}
test2_first_occurance = {"input":{"_list":[1,1,1,1,2,2,3,4,5,6,7],"_target":1},"output":0}
test2_last_occurance =  {"input":{"_list":[1,1,1,1,2,2,3,4,5,6,7],"_target":1},"output":3}
test3_first_occurance = {"input":{"_list":list(range(0,10000000)), "_target":9999998},"output":9999998}
test3_last_occurance =  {"input":{"_list":list(range(0,10000000)), "_target":9999998},"output":9999998}

res,passed,runtime = evaluate_test_case(get_first_index,test1_first_occurance,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))
res,passed,runtime = evaluate_test_case(get_last_index,test1_last_occurance,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))


res,passed,runtime = evaluate_test_case(get_first_index,test2_first_occurance,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))
res,passed,runtime = evaluate_test_case(get_last_index,test2_last_occurance,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))

res,passed,runtime = evaluate_test_case(get_first_index,test3_first_occurance,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))
res,passed,runtime = evaluate_test_case(get_first_index,test3_last_occurance,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))

# produces given result:
# O/P: 2 result: True  runtime: 0.025
# O/P: 5 result: True  runtime: 0.013
# O/P: 0 result: True  runtime: 0.004
# O/P: 3 result: True  runtime: 0.003
# O/P: 9999998 result: True  runtime: 0.018
# O/P: 9999998 result: True  runtime: 0.026