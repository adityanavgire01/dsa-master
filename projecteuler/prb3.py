# Largest Prime Factor
#  Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?

# what is prime factor : 
# prime numebrs - natural numbers that are divisible by 1 and itself
# to write a number as a product of its prime factors
# 2 methods - repeated division, buidling a factor tree

# eg 180 - repeated div method  -> 180/2 = 90 -> 90/2 = 45 -> 45/3 = 15 -> 15/3 = 5 -> 5/5 = 1 
 
def largest_prime_factor(n):
    factor = 2
    largest = 0

    # remove factors of 2 first
    while n % factor == 0:
        largest = factor
        n //= factor

    # check for odd factors starting from 3
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2

    # If n is still greater than 2, it is the largest prime factor
    if n > 2:
        largest = n

    return largest

number = 600851475143
print(largest_prime_factor(number))