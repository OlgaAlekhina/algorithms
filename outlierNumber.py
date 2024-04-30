def outlier_number(nums):
    if nums[0] % 2 != nums[1] % 2:
        return nums[0] if nums[1] % 2 == nums[2] % 2 else nums[1]
    for num in nums:
        if num % 2 != nums[0] % 2:
            return num


print(outlier_number([161, 3, 1719, 19, 11, 13, 20, -21]))
