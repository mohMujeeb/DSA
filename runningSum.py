def runningSum(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * 2
    return nums


nums = [1, 2, 3, 4]

print(runningSum(nums))
print("hello world")