def productExceptSelf(nums):
    n = len(nums)
    output = [0] * n
    output[0] = 1
    for i in range(1, n):
        output[i] = nums[i - 1] * output[i - 1]
    R = 1
    for i in reversed(range(n)):
        output[i] = output[i] * R
        R *= nums[i]
    return output

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(productExceptSelf(nums))

#Runtime: 240 ms, faster than 99.05% of Python3 online submissions for Product of Array Except Self.