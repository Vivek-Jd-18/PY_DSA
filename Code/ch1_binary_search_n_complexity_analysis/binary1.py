from jovian.pythondsa import evaluate_test_case

def binary_search(_list, _target):
    low, high = 0, len(_list)-1
    
    while low <= high:
        mid_index = (low+high) //2
        mid_val = _list[mid_index]

        if mid_val == _target:
            return mid_index
        elif mid_val < _target:
            low = mid_index + 1
        elif mid_val > _target:
            high = mid_index - 1
    
    return -1

test1 = {"input":{"_list":[1,2,3,4],"_target":2},"output":1}
test2 = {"input":{"_list":[11,23,34,45,67,89,90],"_target":89},"output":5}
test3 = {"input":{"_list":[1,2,3,4],"_target":2},"output":1}
test4 = {'input':{'_list':[3,6,9,12,16,18,23,34,56,78,90,99],'_target':100},'output':-1}
test5 = {'input':{'_list':[3,6,9,12,16,18,23,34,56,78,90,99,100],'_target':100},'output':12}
test6 = {'input':{'_list':[3,6,9,12,16,18,23,34,56,78,90,99,100],'_target':3},'output':0}
test7 = {'input':{'_list':[3,6,9,12,16,18,23,34,56,78,90,99,100],'_target':90},'output':10}

evaluate_test_case(binary_search,test1)
evaluate_test_case(binary_search,test2)
evaluate_test_case(binary_search,test3)
evaluate_test_case(binary_search,test4)
evaluate_test_case(binary_search,test5)
evaluate_test_case(binary_search,test6)
evaluate_test_case(binary_search,test7)