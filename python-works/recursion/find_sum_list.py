def find_sum_list(list, size):
    if size == 0:
        return 0
    return list[size-1] + find_sum_list(list=list, size=size-1)


def find_sum_list_2(list):
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        return list[0] + find_sum_list_2(list[1:])
    
if __name__ == '__main__':
    my_list = [9,5]
    print(find_sum_list(list=my_list, size=len(my_list)))
    print(find_sum_list_2(list=my_list))
