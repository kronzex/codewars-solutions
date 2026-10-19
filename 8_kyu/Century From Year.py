"""
Task: Century From Year

Description:

Given a year, return the century it is in.

Examples

1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28
"""

def century(year):
    # Finish this :)
    centuryy = 1
    years_100 = 100
    while year > years_100:
        centuryy += 1
        years_100 += 100
    return centuryy

# test
print(century(1705)) # must output 18
print(century(1900)) # must output 19
print(century(1601)) # must output 17
print(century(2000)) # must output 20
print(century(356)) # must output 4
print(century(89)) # must output 1