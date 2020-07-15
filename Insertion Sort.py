nums = [12, 11, 13, 5, 6]

for i in range(1, len(nums)):
    key = nums[i]

    j = i-1
    while j >=0 and key < nums[j]:
        nums[j+1] = nums[j]
        j -= 1
        print('array in while:' ,nums)
    nums[j+1] = key
    print('array in for:' ,nums, key)