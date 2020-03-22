def sum13(nums):
    sum = 0
    for i in range(len(nums)):
        if nums[i] == 13:
            try:
                nums[i + 1] = 0
            except:
                continue
        else:
            sum += nums[i]
    return sum
