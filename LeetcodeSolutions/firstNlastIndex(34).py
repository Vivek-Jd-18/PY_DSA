class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
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
                    if _list[mid-1] == _target and mid > 0:
                        return 'left'
                    else:
                        return 'found'
                elif _list[mid] < _target:
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
         
        def result(first_indexer, last_indexer):
            return [first_indexer(nums, target), last_indexer(nums, target)]
        
        return result(fetch_first_index,fetch_last_index)
        
