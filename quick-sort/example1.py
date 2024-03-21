def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
    return arr
    
def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1
        while elements[end] > pivot:
            end-=1
        if start < end:
            elements = swap(start, end, elements)
    elements = swap(pivot_index, end, elements)
    return end

def quick_sort(elements, start, end):
    if start < end:
        pivot_index = partition(elements, start, end)
        elements = quick_sort(elements, start, pivot_index-1)
        elements = quick_sort(elements, pivot_index+1, end)
    return elements

    

if __name__ == '__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        print(f'unsorted array: {elements}')
        elements = quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
        print("")