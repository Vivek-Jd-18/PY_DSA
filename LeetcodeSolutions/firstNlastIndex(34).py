
def generic_binary(low, high, condition):
        while(low <= high):
            mid = (low+high) // 2
            res = condition(mid)
            if res == 'found':
                return mid
            elif res == 'left':
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
def fetch_first_index(_list, _target):
    def condition(mid):
        if _list[mid] == _target:
            if mid > 0 and _list[mid-1] == _target:
                return 'left'
            else:
                print("second")
                return 'found'
        elif _list[mid] < _target:
            print("third")
            return 'right'
        else:
            return 'left' 
    return generic_binary(0, len(_list)-1, condition)

def fetch_last_index(_list, _target):
    def condition(mid):
        if _list[mid] == _target:
            if mid < len(_list)-1 and _list[mid+1] == _target:
                return 'right'
            else:
                return 'found'
        elif _list[mid] < _target:
            return 'right'
        else:
            return 'left' 
    return generic_binary(0, len(_list)-1, condition)

# test0 = [5,7,7,8,8,10]
test0 = [1]
    
def result(first_indexer, last_indexer):
    return [first_indexer(test0, 1), last_indexer(test0, 1)]

print(result(fetch_first_index,fetch_last_index))


# print(fetch_first_index(test0, 1))