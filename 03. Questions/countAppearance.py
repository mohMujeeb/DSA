# Count how many times a number appears in the array.
"""
    arr = [2, 3, 4, 5, 4, 2, 3, 4, 5]
    number = 4
    where 4 appears 3 times in the array so three will be returned
"""

def countAppear(number , arr):
    cnt = 0
    ran = len(arr)
    for i in range(ran):
        if arr[i] == number:
            cnt = cnt + 1
    return cnt

arr = [2, 3, 4, 5, 4, 2, 3, 4, 5]
number = 4

print(countAppear(number, arr))

