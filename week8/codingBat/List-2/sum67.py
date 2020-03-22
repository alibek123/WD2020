def sum67(nums):
    sum = 0
    none = False

    for i in range(0, len(nums)):
        if not none:
            if nums[i] == 6:
                none = True
            else:
                sum += nums[i]
        else:
            if nums[i] == 7:
                none = False
    return sum
