# Largest Palindrome Product
#  Problem 4
#  A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.

# code 

# function to check palindrome: 

def is_palindrome(n):
    return str(n) == str(n)[::-1]  # Check if the number reads the same forward and backward

def largest_palindrome_product():
    largest_palindrome = 0  # To store the largest palindrome
    factors = (0, 0)  # To store the pair of numbers that produce the palindrome

    # Iterate over all 3-digit numbers in reverse order
    for a in range(999, 99, -1):  # From 999 down to 100
        for b in range(a, 99, -1):  # Start from 'a' to avoid duplicate checks (e.g., 912x910 vs 910x912)
            product = a * b
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                factors = (a, b)

    return largest_palindrome, factors  # Return the largest palindrome and the numbers that produced it

# Example Usage
result, (x, y) = largest_palindrome_product()
print(f"Largest Palindrome: {result} (Product of {x} and {y})")
