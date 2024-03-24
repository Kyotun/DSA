def find_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def find_sum_rec(n):
    if n == 1:
        return n
    return n + find_sum_rec(n-1)

if __name__ == '__main__':
    print(find_sum(n=5))
    print(find_sum_rec(n=5))