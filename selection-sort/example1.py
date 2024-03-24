def find_min_element(array, start, end):
    min = array[start]
    min_index = start
    for index in range(start,end):
        if array[index] < min:
            min = array[index]
            min_index = index
    return min, min_index

def selection_sort(array):
    for i in range(0, len(array)):
        temp = array[i]
        array[i], index = find_min_element(array=array, start=i, end=len(array))
        array[index] = temp

if __name__ == '__main__':
    elements = [78,12,15,8,61,53,23,27]
    selection_sort(elements)
    print(elements)