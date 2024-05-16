def my_func(elements, L, R):
    if R <= L:
        return elements
    pivot = elements[L]
    left = L
    right = R
    while left < right:
        while elements[left] < pivot:
            left += 1
        while elements[right] > pivot:
            right -= 1
        print(f"elements1: {elements}")
        elements = my_func_swap(elements, left, right)
        print(f"elements2: {elements}")
    temp = elements[right]
    print(f"")
    elements[L] = elements[left]
    elements[left] = temp
    elements[right] = pivot
    print(f"elements3: {elements}")
    elements = my_func(elements, L, right - 1)
    elements = my_func(elements, right + 1, R)
    return elements


def my_func_swap(elements, L, R):
    temp = elements[L]
    elements[L] = elements[R]
    elements[R] = temp
    return elements


if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    my_array = [6, 8, 3, 9, 2, 1, 4, 5, 7]
    my_array2 = [8, 6, 3, 7, 4, 2, 20, -45]
    my_array3 = [3, 5, 2, 6, 1, 7, 4]
    print(len(my_array3) / 2)
