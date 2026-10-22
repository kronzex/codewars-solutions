"""
Task: Even or Odd

Description:

Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""
# solution
def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'

# test
print(even_or_odd(1)) # must output Odd
print(even_or_odd(2)) # must output Even
print(even_or_odd(-1)) # must output Odd
print(even_or_odd(-2)) # must output Even
print(even_or_odd(0)) # must output Even