"""
Task: Multiples of 3 or 5

Description:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If a number is a multiple of both 3 and 5, only count it once.
"""
# solution
def solution(n):
    """
    Возвращает сумму всех натуральных чисел меньше n,
    которые кратны 3 или 5.
    Если n <= 0, возвращает 0.
    """
    if n <= 0:
        return 0
    total = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# test
print(solution(4)) # must output 3
print(solution(6)) # must output 8
print(solution(16)) # must output 60
print(solution(3)) # must output 0
print(solution(5)) # must output 3