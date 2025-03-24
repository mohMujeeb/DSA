# Python program to print numbers in reversed order without using loops.

def print_reverse(n):
    if n == 0:
        return 
    print(n, end=" ")
    print_reverse(n - 1)
    
print_reverse(10)