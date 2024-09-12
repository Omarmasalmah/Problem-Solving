def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10
    if carry:
        digits.insert(0, carry)
    return digits

#main function
if __name__ == '__main__':
    print(plusOne([1,2,3])) # [1,2,4]
    print(plusOne([4,3,2,1])) # [4,3,2,2]
    print(plusOne([9])) # [1,0]
    print(plusOne([9,9]))