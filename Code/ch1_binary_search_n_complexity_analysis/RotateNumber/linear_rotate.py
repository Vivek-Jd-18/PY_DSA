# time complexity  O(n)

from jovian.pythondsa import evaluate_test_case

# def find_rotation(_list):
#     count = 1
#     rotations = 0
#     while count < len(_list):
#         print(_list[count] , _list[count-1])
#         if  _list[count] > _list[count-1]:
#             return rotations
#         rotations+=1
#         count+=1
#     return rotations

def find_rotation(_list):
    rotations = 0
    while rotations < len(_list):
        # print(_list[rotations] , _list[rotations-1])
        if  _list[rotations] < _list[rotations-1]:
            return rotations
        rotations+=1
    return 0

test0 = {"input":{"_list":[19,25,29,3,5,6,7,9,11,14]},"output":3}
test1 = {"input":{"_list":[2,3,4,1]},"output":3}
test2 = {"input":{"_list":[5,6,7,8,1,2,3,4]},"output":4}
test3 = {"input":{"_list":[8,9,10,1,2,3,4,5,6,7]},"output":3}
test4 = {"input":{"_list":[3,4,5,6,7,8,9,10,1,2]},"output":8}
test5 = {"input":{"_list":[1,2,3,4,5]},"output":0}
# test6 = {"input":{"_list":[5,4,3,2,1]},"output":4}
test7 = {"input":{"_list":[1,2,3,4,5,6,7,8,9,10]},"output":0}

evaluate_test_case(find_rotation,test0)
evaluate_test_case(find_rotation,test1)
evaluate_test_case(find_rotation,test2)
evaluate_test_case(find_rotation,test3)
evaluate_test_case(find_rotation,test4)
evaluate_test_case(find_rotation,test5)
# evaluate_test_case(find_rotation,test6)
evaluate_test_case(find_rotation,test7)

