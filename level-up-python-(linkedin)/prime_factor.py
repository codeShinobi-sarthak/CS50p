def get_prime_factors(num):
    d = 2
    factors = []

    while(num != 1):
        if(num % d == 0):
            num /= d
            factors.append(d)
        else:
            d += 1

    return factors


if __name__ == "__main__":
    print(get_prime_factors(630))
    print(get_prime_factors(15))