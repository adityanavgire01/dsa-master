# Sum Square Difference 
# Problem 6 
# The sum of the squares of the first ten natural numbers is, 12+22+...+102 = 385. The square of the sum of the first ten natural numbers is, (1+2+...+10)2 = 552 = 3025. Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sumofsquares():

    squares = []
    total_sum = 0
    for i in range(101):
        squares.append(i**2)

    for i in squares:
        total_sum += i

    return total_sum

def squareofsum():

    total_sum = 0
    nums = []
    for i in range(101):
        nums.append(i)

    for i in nums:
        total_sum += i

    return total_sum**2

print(sumofsquares())
print(squareofsum())

print(squareofsum()-sumofsquares())


# more optimized code - 
# using formular - to calucalte the sum of first n natural numbers
# and to calcualte th sum of squares of numbers
