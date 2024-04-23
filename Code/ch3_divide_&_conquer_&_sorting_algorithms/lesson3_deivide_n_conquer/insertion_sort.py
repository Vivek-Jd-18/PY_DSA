# Inserttion sort
# task: write a function to sort numbers in increasing order

def insertion_sort(list:list)->list:
    for i in range(1, len(list)):
        j = i

        while j > 0 and list[j-1] > list[j]:
            list[j-1], list[j] = list[j], list[j-1]
            j-=1

unsorted1 = [7,9,5,2,4,1]
insertion_sort(unsorted1)
print(unsorted1)