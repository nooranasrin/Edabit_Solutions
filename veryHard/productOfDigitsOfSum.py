# Create a function that takes numbers as arguments, adds them together,
# and returns the product of digits until the answer is only 1 digit long.

from functools import reduce
import operator


def sum_dig_prod(*args):
    product = sum(args)
    while product > 9:
        product = reduce(operator.mul, [int(num) for num in str(product)])
    return product


def main():
    print(sum_dig_prod(16, 28))
    print(sum_dig_prod(0))
    print(sum_dig_prod(1, 2, 3, 4, 5, 6))


main()

