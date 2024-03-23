def merge_sort(array, key=None, descending=False):
    if len(array) <= 1:
        return
    
    mid = len(array)//2
    right = array[mid:]
    left = array[:mid]

    merge_sort(left, key, descending)
    merge_sort(right, key, descending)

    merge_two_sorted_lists(left, right, array, key, descending)


def merge_two_sorted_lists(left_child, right_child, parent_array, key=None, descending=False):
    if parent_array[0][key]:
        pass
    else:
        raise Exception("Unknown key value. Please give a valid key.")
    len_left = len(left_child)
    len_right = len(right_child)

    i = j = k = 0

    while i < len_left and j < len_right:
        if descending:
            if left_child[i][key] <= right_child[j][key]:
                parent_array[k]= right_child[j]
                j+=1
            else:
                parent_array[k]= left_child[i]
                i+=1
        else:
            if left_child[i][key] <= right_child[j][key]:
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
    elements = [
            { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
            { 'name': 'rajab', 'age': 12,  'time_hours': 3},
            { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
            { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
        ]
    merge_sort(array=elements, key='name')
    print(elements)