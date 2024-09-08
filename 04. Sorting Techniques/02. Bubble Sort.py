"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly 
swapping the adjacent elements if they are in the wrong order.

In Bubble Sort algorithm, 
- traverse from left and compare adjacent elements and the higher one 
is placed at right side. 
- In this way, the largest element is moved to the rightmost end at first. 
- This process is then continued to find the second largest and place it 
and so on until the data is sorted.

Input = [6, 0, 3, 5]
Output = [0, 3, 5, 6]

No of Passes = n - 1
No of comparisons = n * (n - 1) / 2

Time complexity = O(N^2)
Auxiliary space = O(1)
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

arr = [6, 0, 3, 5]
print(bubbleSort(arr))