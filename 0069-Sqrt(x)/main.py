def mySqrt(x):
    if 0 == x:
        return 0
    if x == 1:
            return 1
    left, right = 1, x
    while left < right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid
    return left - 1

print(mySqrt(8))
print(mySqrt(4))
print(mySqrt(0))
print(mySqrt(1))
print(mySqrt(9))