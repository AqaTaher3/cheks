def prime_factors_with_count(number):
    factors = {}
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            number //= divisor
        else:
            divisor += 1
    return factors

# مثال
number = 10406775




print("Prime divisors of", number, "are:", prime_factors_with_count(number))
