# task: write a function to sort numbers in increasing order 

# ip = [5,3,7,9,4,1,2]
# op = [1,2,3,4,5,7,9]

def sorter(list):
    li=[]
    if len(list) == 1:
        return list
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j]> list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print([5,3,7,9,4,1,2])
print(sorter([5,3,7,9,4,1,2]))




print([6,5,6,6,5,4,-1,-11,-239,0,0,4,3,212])
print(sorter([6,5,6,6,5,4,-1,-11,-239,0,0,4,3,212]))

# complexities

#   `Time Complexity`               |    `Space Complexity`
#   (n-1)*(n-1)                     |    overall is O(n)
#   (n-1)^2                         |    additional is O(1) 
#   n^2 - 2n +1                     |
#   O(n^2)  Quadratic Complexity    |

