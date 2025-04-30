def digit_count(num):
    
    result = 0
    while num > 0:
        print(f"Current Number: {num}")
        digit = num % 10
        print(f"Digit: {digit}")
        result = result * 10 + digit
        print(f"Result: {result}")
        num = num // 10
        print(f"Final Result: {num}")
    return result

print(digit_count(793))