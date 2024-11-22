# here prblms with imp

# prblm 3 -> prime factors

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
print(gcd(1005,105))