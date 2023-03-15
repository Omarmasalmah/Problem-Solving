def longestConsecutive(self, nums):
    if not nums:
        return 0
    nums = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in nums:
            current = num
            current_longest = 1
            while current + 1 in nums:
                current += 1
                current_longest += 1
            longest = max(longest, current_longest)
    return longest

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums))