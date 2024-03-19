from jovian.pythondsa import evaluate_test_case

def linear_search(_list,_target):
    index = 0
    while index < len(_list):
        if _target == _list[index]:
            return index
        index += 1
    return -1

def filter_duplicates(_list, _target, _mid_index, _mid_value):
    if _target == _mid_value:
        if _mid_index-1 >= 0 and _list[_mid_index-1] == _target:
            return -1
        else:
            return 0
    if _mid_value < _target:
        return 1
    else:
        return -1
    
def binary_search(_list,_target):
    low, high = 0, len(_list) - 1
    while low<= high:
        mid_index = (low+high) //2
        mid_value = _list[mid_index]

        res = filter_duplicates(_list, _target, mid_index, mid_value)

        if res == 0:
            return mid_index
        elif res == -1:
            high = mid_index - 1
        elif res == 1:
            low = mid_index + 1
    return -1


test1 = {"input":{"_list":[1,2,3,4],"_target":2},"output":1}
test2 = {"input":{"_list":[11,23,34,45,67,89,90],"_target":89},"output":5}
test3 = {"input":{"_list":list(range(0,10000000)), "_target":9999998},"output":9999998}

res,passed,runtime = evaluate_test_case(linear_search,test1,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))
res,passed,runtime = evaluate_test_case(binary_search,test1,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))

res,passed,runtime = evaluate_test_case(linear_search,test2,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))
res,passed,runtime = evaluate_test_case(binary_search,test2,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))

res,passed,runtime = evaluate_test_case(linear_search,test3,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))
res,passed,runtime = evaluate_test_case(binary_search,test3,display=False)
print("O/P: {} result: {}  runtime: {}".format(res,passed,runtime))


# O/P: 1 result: True  runtime: 0.026
# O/P: 1 result: True  runtime: 0.012
# O/P: 5 result: True  runtime: 0.007
# O/P: 5 result: True  runtime: 0.007
# O/P: 9999998 result: True  runtime: 1543.178
# O/P: 9999998 result: True  runtime: 0.021

# as you can see Binary Search is 73484.666666667 times faster than the Linear search