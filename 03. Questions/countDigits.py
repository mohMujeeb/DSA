########################################
"""You are given a number. You need to count number of digits in it.

Example 1:

Input:
n = 4567
Output: 4

Example 2:

Input:
n = 987
Output: 3

"""
########################################

def count_digits(n):   # function creation which takes a number
    count = 0 # count number of digits
    while n > 0:
        l_digit = n % 10
        n = n // 10
        
        count += 1
    return count

print(f"Example 1 with input number 4567 have {count_digits(4567)} digits")
print(f"Example 2 with input number 987 have {count_digits(987)} digits")
