def primeFactors(n):
    factors = []
    l = 2
    while l ** 2 <= n:
        while (n % l) == 0:
            factors.append(l)
            n //= l
        l += 1
    if n > 1:
       factors.append(n)
    return factors


def sumOfDigits(n):
    if n == 0:
        return 0
    return n % 10 + (sumOfDigits(n // 10))

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

def isSmithNumber(n):
    if isPrime(n):
        return 0
    else:
        factors = primeFactors(n)
        result = 0
        for i in range(len(factors)):
            result  += sumOfDigits(factors[i])
        if result == sumOfDigits(n):
            return 1
        return 0

a = input()
a = int(a)
print(isSmithNumber(a))

