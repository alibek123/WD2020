def centered_average(nums):
    sum = 0
    i_max = nums.index(max(nums))
    i_min = nums.index(min(nums))

    for i in range(0, len(nums)):
        if i != i_max and i != i_min:
            sum += nums[i]

    no = 2 if i_max != i_min else 1
    return sum / (len(nums) - no)
