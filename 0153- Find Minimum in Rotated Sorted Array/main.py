def findMin(nums):
    if len(nums) == 1:
        return nums[0]
    if nums[0] < nums[-1]:
        return nums[0]
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1

if __name__ == '__main__':
    print(findMin([3,4,5,1,2]))
    print(findMin([4,5,6,7,0,1,2]))
    print(findMin([11,13,15,17]))
    print(findMin([1]))
    print(findMin([2,1]))
    print(findMin([3,1,2]))
    print(findMin([1,2,3]))
    print(findMin([2,3,4,5,1]))
    print(findMin([4,5,6,7,0,1,2]))