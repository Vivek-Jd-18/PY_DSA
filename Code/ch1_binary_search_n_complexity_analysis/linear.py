# problem: finding a position of an element in an array

from jovian.pythondsa import evaluate_test_case

# linear search
def linear_serach(_list,_target):
    for i in range(len(_list)):
        if _list[i] == _target:
            return i
    return -1        

# making 5 test cases
test1 = {'input':{'_list':[1,2,3,4,5],'_target':3},'output':2}
test2 = {'input':{'_list':[3,6,9,12,16,18,23,34,56,78,90,99],'_target':100},'output':-1}
test3 = {'input':{'_list':[3,6,9,12,16,18,23,34,56,78,90,99,100],'_target':100},'output':12}
test4 = {'input':{'_list':[3,6,9,12,16,18,23,34,56,78,90,99,100],'_target':3},'output':0}
test5 = {'input':{'_list':[3,6,9,12,16,18,23,34,56,78,90,99,100],'_target':90},'output':10}

evaluate_test_case(linear_serach,test1)
evaluate_test_case(linear_serach,test2)
evaluate_test_case(linear_serach,test3)
evaluate_test_case(linear_serach,test4)
evaluate_test_case(linear_serach,test5)