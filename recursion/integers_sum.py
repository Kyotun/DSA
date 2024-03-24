def sum_integer(num):
    if num == 0:
        return 0
    return num % 10 + sum_integer(num//10)

if __name__ == '__main__':
    print(sum_integer(num=1111))