def sum_pos_integers(high_end):
    if high_end <= 0:
        return 0
    return high_end + sum_pos_integers(high_end=high_end-2)

if __name__ == '__main__':
    test_cases = [0, 1, 9, 19, 99, 111,]
    for element in test_cases:
        print(f"High end: {element}, sum: ", sum_pos_integers(high_end=element))