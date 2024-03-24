def to_string(n, base):
    hexa_list = "0123456789ABCDEF"

    if n < base:
        return hexa_list[n]
    else:
        return to_string(n // base, base) + hexa_list[n % base]

if __name__ == '__main__':
    print(to_string(2394, base=16))