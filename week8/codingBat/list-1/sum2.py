def sum2(nums):
    sum = 0
    if len(nums) == 0:
        return 0
    elif len(nums) <= 2:
        for i in nums:
            sum += i
    else:
        for i in range(2):
            sum += nums[i]
    return sum