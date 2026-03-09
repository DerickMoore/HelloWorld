def dm_hello(s):
    print(s)


dm_hello("Hello, world !")

#  create a function that works out if an interger parameter is prime or not  
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# test the function with some numbers
print(is_prime(1))  # False     
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(4))  # False
print(is_prime(5))  # True
print(is_prime(10)) # False
print(is_prime(11)) # True
