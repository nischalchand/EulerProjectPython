# answer - 4179871

# Algorithm:
# 1. Get all abundant numbers
# 2. Add all to get sums and mark the corresponding array to being abundant sum
# 3. The left out are non-abundant, add them

from utils import Euler

MAX, SUM = 20161, 0

abundant_numbers = set()


def is_abundant_sum(x):
    for a in abundant_numbers:
        if x - a in abundant_numbers:
            return True
    return False


for n in range(1, MAX + 1):
    if Euler.sum_of_divisors(n, True) > n:
        abundant_numbers.add(n)
    if not is_abundant_sum(n):
        SUM += n

print(SUM)
