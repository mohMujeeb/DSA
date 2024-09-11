# Python Program to print 1 to N numbers without loops.

def count_up(n):
    if n == 0:
        return 
    count_up(n - 1)
    print(n, end=" ")

n = 10    
count_up(n)