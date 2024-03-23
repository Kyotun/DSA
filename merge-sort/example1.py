def merge_sort(array):
    if len(array) <= 1:
        return
    
    mid = len(array)//2
    right = array[mid:]
    left = array[:mid]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, array)

def merge_two_sorted_lists(left_child, right_child, parent_array):
    len_left = len(left_child)
    len_right = len(right_child)

    i = j = k = 0

    while i < len_left and j < len_right:
        if left_child[i] <= right_child[j]:
            parent_array[k] = left_child[i]
            i+=1
        else:
            parent_array[k] = right_child[j]
            j+=1
        k+=1
    
    while i < len_left:
        parent_array[k] = left_child[i]
        i+=1
        k+=1
    
    while j < len_right:
        parent_array[k] = right_child[j]
        j+=1
        k+=1
    
if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for array in test_cases:
        merge_sort(array)
        print(array)