def linear_search(numbers_list, target):
    for number in numbers_list:
        if number == target:
            return numbers_list.index(number)
    return -1

def binary_search(numbers_list, target):
    index = 0
    k = 2
    while True:
        if numbers_list[index] < target:
            index += int(len(numbers_list)/k)
        elif numbers_list[index] > target:
            index -= int(len(numbers_list)/k)
        else:
            return index
        
        if index + int(len(numbers_list)/k) == index:
            break
        k *= 2
    return -1

if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 19

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")

    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search")

