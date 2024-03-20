from util import time_it

@time_it
def linear_search(numbers_list, target):
    for number in numbers_list:
        if number == target:
            return numbers_list.index(number)
    raise Exception("Value cannot be found in the given data.")

@time_it
def linear_search_2(number_list, target):
    for index, element in enumerate(number_list):
        if element == target:
            return index
    raise Exception("Value cannot be found in the given data.")

@time_it
def binary_search(number_list, target):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = (left_index + right_index) // 2

    while left_index <= right_index:
        if number_list[mid_index] == target:
            return mid_index
        elif number_list[mid_index] > target:
            right_index = mid_index - 1
        elif number_list[mid_index] < target:
            left_index = mid_index + 1
        mid_index = (left_index + right_index) // 2
    raise Exception("Value cannot be found in the given data.")

@time_it
def find_all_occurances(number_list, target):
    index = binary_search(numbers_list, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers_list[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers_list):
        if numbers_list[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

@time_it
def binary_search_recursive(number_list, target, left_index, right_index):
    if right_index < left_index:
        raise Exception("Value cannot be found in the given data.")
    
    mid_index = (left_index + right_index) // 2
    if mid_index >= len(number_list) or mid_index < 0:
        raise Exception("Value cannot be found in the given data.")
    
    mid_number = number_list[mid_index]

    if mid_number == target:
        return mid_index

    if mid_number > target:
        right_index = mid_index - 1
    elif mid_number < target:
        left_index = mid_index + 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

    

if __name__ == '__main__':
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15  
    
    print(find_all_occurances(numbers_list, number_to_find))

    index = linear_search(numbers_list, number_to_find)
    index = linear_search_2(numbers_list, number_to_find)
    index = binary_search(numbers_list, number_to_find)
    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))



