
def searchIndex(nums,target):
    # nums are sort
    if not nums:
        return 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

print(searchIndex([1,3,5,6],5)) # 2
print(searchIndex([1,3,5,6],2)) # 1
print(searchIndex([1,3,5,6],7)) # 4