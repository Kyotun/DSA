def calc_gcd(num1, num2):
    low = min(num1, num2)
    high = max(num1, num2)

    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return calc_gcd(low, high % low)

if __name__ == '__main__':
    print(calc_gcd(5,10))
