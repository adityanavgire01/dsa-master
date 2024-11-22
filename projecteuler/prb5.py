# Smallest Multiple
#  Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

# evenly divisible = x is said to be evenly divisible by y if x/y results in a whole number with no remainder

# to be continued : https://chatgpt.com/c/66ed59ce-225c-800f-92cc-20a7714c499f


def gcd(a,b):
    # inplementation of Eucledian algo for GCD
    while b != 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    # calculating LCM using formula : LCM(a, b) = (a*b) // GCD(a, b)
    return (a*b) // gcd(a, b)

def smallest_multiple(n):
    result = 1
    for i in range(1, n+1):
        result = lcm(result, i)
    return result

print(smallest_multiple(20))