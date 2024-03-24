def find_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def find_sum_rec(n):
    if n == 1:
        return n
    return n + find_sum_rec(n-1)

# 0, 1, 1, 2, 3, 5, 8, 13, 21
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    

if __name__ == '__main__':
    print(find_sum(5))
    print(find_sum_rec(5))
    print(fibonacci(n=7))