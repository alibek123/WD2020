def big_diff(nums):
    max = -1
    min = 1000
    for i in nums:
        if i > max:
            max = i
        if i < min:
            min = i
    return max - min
