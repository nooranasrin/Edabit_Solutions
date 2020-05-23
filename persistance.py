# The additive persistence of an integer, n, is the number of times you have to replace n with the sum of its digits until n becomes a single digit integer.
#
# The multiplicative persistence of an integer, n, is the number of times you have to replace n with the product of its digits until n becomes a single digit integer.
#
# Create two functions that take an integer as an argument and:
#
# 1. Return its additive persistence.
# 2. Return its multiplicative persistence.


import operator
from functools import reduce


def multiplicative_persistence(n):
    iterations = 0
    while n > 9:
        n = reduce(operator.mul, [int(num) for num in str(n)])
        iterations += 1
    return iterations


def additive_persistence(n):
    iterations = 0
    while n > 9:
        n = reduce(operator.add, [int(num) for num in str(n)])
        iterations += 1
    return iterations


print(additive_persistence(1679583))
print(additive_persistence(123456))
print(additive_persistence(6))

print(multiplicative_persistence(77))
print(multiplicative_persistence(123456))
print(multiplicative_persistence(4))
