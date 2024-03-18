from jovian.pythondsa import evaluate_test_case

def filter_duplicates(_list, _target, _mid_index):
    if _list[_mid_index] == _target:
        if _list[_mid_index-1] == _target and _mid_index-1 >= 0:
            return -1
        else:
            return 0
    elif _list[_mid_index] < _target:
        return 1
    else:
        return -1

def binary_ad(_list,_target):
    low, high = 0, len(_list) - 1

    while low <= high:
        mid_index = (low+high) // 2

        res = filter_duplicates(_list, _target, mid_index)

        if res == 0:
            return mid_index
        elif res == 1:
            low = mid_index + 1
        elif res == -1:
            high = mid_index -1

    return -1

test0 = {"input":{"_list":[1,2,3,4,4,4,4,5,6,6,6,7,8,9],"_target":4},"output":3}
test1 = {'input':{'_list':[1,2,3,4,4,4,5,5,5,5,5,5,6,6,6,7,7,7,8,8,9,10],"_target":5},'output':6}
test2 = {
  "input": {
    "_list": [1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 9, 10],
    "_target": 4
  },
  "output": 5
}
test3 = {
  "input": {
    "_list": [1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9],
    "_target": 1
  },
  "output": 0
}
test4 = {
  "input": {
    "_list": [1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 7, 8, 9, 10],
    "_target": 7
  },
  "output": 9
}
test5 = {
  "input": {
    "_list": [1, 1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 8, 8, 8, 9],
    "_target": 8
  },
  "output": 13
}
test6 = {
  "input": {
    "_list": [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 8, 9],
    "_target": 3
  },
  "output": 5
}
test7 = {
  "input": {
    "_list": [1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 6, 6, 7, 7, 7, 7, 8, 9, 9, 10],
    "_target": 4
  },
  "output": 3
}


evaluate_test_case(binary_ad,test0)
evaluate_test_case(binary_ad,test1)
evaluate_test_case(binary_ad,test2)
evaluate_test_case(binary_ad,test3)
evaluate_test_case(binary_ad,test4)
evaluate_test_case(binary_ad,test5)
evaluate_test_case(binary_ad,test6)
evaluate_test_case(binary_ad,test7)