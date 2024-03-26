def cal_harmonic(n_term):
    if n_term == 1:
        return 1
    return 1/n_term + cal_harmonic(n_term=n_term-1)

if __name__ == '__main__':
    print(cal_harmonic(n_term=4))
