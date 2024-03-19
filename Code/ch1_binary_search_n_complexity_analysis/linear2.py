# using while loop

from jovian.pythondsa import evaluate_test_case

def linear_search(data, target):
    cursor = 0
    while cursor <= len(data) - 1:
        if target == data[cursor]:
            return cursor
        cursor += 1

test1 = {'input':{'data':[1,2,3,4,5],'target':3},'output':2}
test2 = {'input':{'data':[3,6,9,12,16,18,23,34,56,78,90,99],'target':100},'output':-1}
test3 = {'input':{'data':[3,6,9,12,16,18,23,34,56,78,90,99,100],'target':100},'output':12}
test4 = {'input':{'data':[3,6,9,12,16,18,23,34,56,78,90,99,100],'target':3},'output':0}
test5 = {'input':{'data':[3,6,9,12,16,18,23,34,56,78,90,99,100],'target':90},'output':10}

evaluate_test_case(linear_search,test1)
evaluate_test_case(linear_search,test2)
evaluate_test_case(linear_search,test3)
evaluate_test_case(linear_search,test4)
evaluate_test_case(linear_search,test5)