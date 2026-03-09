"""Module for utility functions: hello world printer and prime number checker."""
from dm_func import dm_hello
from dm_func import is_prime




dm_hello("Hello, world !")




# test the function with some numbers
print(is_prime(1))  # False
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(4))  # False
print(is_prime(5))  # True
print(is_prime(10)) # False
print(is_prime(11)) # True
