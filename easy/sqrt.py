def mySqrt(x: int) -> int:

    if x == 0:
        return x

    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid

        if mid * mid >= x:
            right = mid - 1
        else:
            left = mid + 1
    
    return right