def sum_rec_list(my_list):
    if len(my_list) == 0:
        return 0
    
    dran = my_list[0]
    if type(dran) == list:
        dran = sum_rec_list(dran)
    return dran + sum_rec_list(my_list[1:])

if __name__ == '__main__':
    my_list = [1, 2, [3,4], [6,7]]
    print(sum_rec_list(my_list=my_list))