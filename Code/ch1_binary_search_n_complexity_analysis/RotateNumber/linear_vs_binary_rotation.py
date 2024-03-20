from jovian.pythondsa import evaluate_test_case

def linear_find_rotation(_list):
    rotations = 0
    while rotations < len(_list):
        if  _list[rotations] < _list[rotations-1]:
            return rotations
        rotations+=1
    return 0

def rotations_by_binary(_list):
    low, high = 0, len(_list)-1
    while(low<=high):
        mid_index = (low + high) // 2

        if _list[mid_index-1] > _list[mid_index]:
            return mid_index
        elif _list[high] < _list[mid_index]:
            low = mid_index + 1
        else:
            high = mid_index - 1
    return 0


list = list(range(1, 100001))
# Rotate the list 95000 times
for i in range(95000):
    list.append(list.pop(0))

test1 = {"input":{"_list":list},"output":0};
test2 = {"input":{"_list":[50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]},"output":11};
test3 = {"input":{"_list":[21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]},"output":40};
test4 = {"input":{"_list":[41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]},"output":20};
test5 = {"input":{"_list":[51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]},"output":10};


a,b,c = evaluate_test_case(linear_find_rotation,test1,display=False)
print("O/P: {} result: {}  runtime: {}".format(a,b,c))
a,b,c = evaluate_test_case(rotations_by_binary,test1,display=False)
print("O/P: {} result: {}  runtime: {}".format(a,b,c))
a,b,c = evaluate_test_case(linear_find_rotation,test2,display=False)
print("O/P: {} result: {}  runtime: {}".format(a,b,c))
a,b,c = evaluate_test_case(rotations_by_binary,test2,display=False)
print("O/P: {} result: {}  runtime: {}".format(a,b,c))
a,b,c = evaluate_test_case(linear_find_rotation,test3,display=False)
print("O/P: {} result: {}  runtime: {}".format(a,b,c))
a,b,c = evaluate_test_case(rotations_by_binary,test3,display=False)
print("O/P: {} result: {}  runtime: {}".format(a,b,c))
a,b,c = evaluate_test_case(linear_find_rotation,test4,display=False)
print("O/P: {} result: {}  runtime: {}".format(a,b,c))
a,b,c = evaluate_test_case(rotations_by_binary,test4,display=False)
print("O/P: {} result: {}  runtime: {}".format(a,b,c))
a,b,c = evaluate_test_case(linear_find_rotation,test5,display=False)
print("O/P: {} result: {}  runtime: {}".format(a,b,c))
a,b,c = evaluate_test_case(rotations_by_binary,test5,display=False)
print("O/P: {} result: {}  runtime: {}".format(a,b,c))

# O/P: 5000 result: False  runtime: 0.778
# O/P: 5000 result: False  runtime: 0.012
# O/P: 11   result: True   runtime: 0.006
# O/P: 11   result: True   runtime: 0.005
# O/P: 40   result: True   runtime: 0.014
# O/P: 40   result: True   runtime: 0.003
# O/P: 20   result: True   runtime: 0.006
# O/P: 20   result: True   runtime: 0.005
# O/P: 10   result: True   runtime: 0.004
# O/P: 10   result: True   runtime: 0.002