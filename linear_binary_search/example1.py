def linear_search(numbers_list, target):
    for number in numbers_list:
        if number == target:
            return numbers_list.index(number)
    raise Exception("Value cannot be found in the given data.")

def linear_search_2(number_list, target):
    for index, element in enumerate(number_list):
        if element == target:
            return index
    raise Exception("Value cannot be found in the given data.")

def binary_search(numbers_list, target):
    index = 0
    k = 2
    while True:
        if numbers_list[index] < target:
            index += len(numbers_list)//k
        elif numbers_list[index] > target:
            index -= len(numbers_list)//k
        else:
            return index
        
        if index + (len(numbers_list)//k) == index:
            break
        k *= 2
    raise Exception("Value cannot be found in the given data.")

def binary_search_2(number_list, target):
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

if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 67

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search.")

    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search.")

    index = binary_search_2(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search 2.")

    index = linear_search_2(number_list=numbers_list, target=number_to_find)
    print(f"Number found at index {index} using linear search 2.")