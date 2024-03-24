def power(base, multiplier):
    if base == 0 and multiplier == 0:
        raise Exception("Base and multiplier cannot be 0 simultaneously.")
    elif base != 0 and multiplier == 0:
        return 1
    if multiplier == 1:
        return base
    return base * power(base, multiplier-1)

if __name__ == '__main__':
    print(power(3,2))