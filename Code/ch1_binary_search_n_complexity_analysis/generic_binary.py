from jovian.pythondsa import evaluate_test_case

def generic_binary(_low, _high, _condition):
    while _low <= _high:
        mid = (_low + _high) // 2
        result = _condition(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            _high = mid - 1
        elif result == 'right':
            _low = mid + 1
    return -1

def find_item(_list, _target):
    def evaluate(_mid):
        if _list[_mid] == _target:
            if _list[_mid-1] == _target and _mid > 0:
                return 'left'
            else:
                return 'found'
        elif _list[_mid] < _target:
            return 'right'
        else:
            return 'left'
    return generic_binary(0, len(_list)-1, evaluate)

test0 = {"input":{"_list":[1,2,3,4],"_target":2},"output":1}
test1 = {"input":{"_list":[1,2,3,4],"_target":2},"output":1}
test2 = {"input":{"_list":[11,23,34,45,67,89,90],"_target":89},"output":5}
test3 = {"input":{"_list":list(range(0,10000000)), "_target":9999998},"output":9999998}

evaluate_test_case(find_item, test0)
evaluate_test_case(find_item, test1)
evaluate_test_case(find_item, test2)
a,b,c = evaluate_test_case(find_item, test3, display=False)
print(a,b,c)