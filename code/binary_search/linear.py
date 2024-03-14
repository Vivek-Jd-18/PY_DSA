from jovian.pythondsa import evaluate_test_case

def linear_search(items, target):
    for i in range(len(items)-1):
        if target == items[i]:
            return i
    return -1

test1 = {'input':{'items':[1,2,4,6,7,8],'target':6},'output':3}
evaluate_test_case(linear_search,test1)