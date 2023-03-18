def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def search2(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        return -1

if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(nums, target))
    print(search2(nums, target))

#Runtime for search:  40 ms
#Runtime for search2:  24 ms
#memory for search2:  13.6 MB
