# 0, 1, 1, 2, 3, 5, 8, 13, 21
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    print(fibonacci(n=6))