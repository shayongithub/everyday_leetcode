""" The nature of the division is the number of times taken to 
    subtract the dividend until the dividend is smaller or equal to the divisor

    Ex: 20 / 4 = 20 - 4 -4 -4 -4 -4 = 0 which takes 5 times

    - The naive silly approach just subtracts the dividend by exact divisor, which cause
        time limit exceeded error (cause by only subtracting it takes a lot of computing power)

    - The improved approach multiplies the divisor by 2, 4, 8 and so on to fasten the processing
        we can use left-shifting bitwise operator to doing this, which is also the heart of the second approach
"""


def divideBitManipulation(dividend: int, divisor: int) -> int:
    if dividend == 0:
        return 0

    sign = 1 if dividend * divisor > 0 else -1
    dividend, divisor = abs(dividend), abs(divisor)

    ans = 0

    while dividend >= divisor:
        curr_divisor, num_divisor = divisor, 1

        while dividend >= curr_divisor:
            dividend -= curr_divisor
            ans += num_divisor

            curr_divisor = curr_divisor << 1
            num_divisor = num_divisor << 1

    ans = ans * sign

    return min(pow(2, 31) - 1, max(pow(-2, 31), ans))


def divideSmartWay(dividend: int, divisor: int) -> int:
    if dividend == 0: 
        return 0

    sign = 1 if dividend * divisor > 0 else -1
    dividend, divisor = abs(dividend), abs(divisor)

    # how about using the range function to solve this problem

    ans = len(range(0, dividend - divisor + 1, divisor))
    ans = ans * sign

    return min(pow(2, 31) - 1, max(pow(-2, 31), ans))


def divideSillyWay(dividend: int, divisor: int) -> int:
    if dividend == 0:
        return 0

    sign = 1 if dividend * divisor > 0 else -1
    ans = 0

    dividend, divisor = abs(dividend), abs(divisor)

    if divisor == 1:
        ans = sign * dividend

        return (
            ans
            if pow(-2, 31) < ans < pow(2, 31) - 1
            else (pow(2, 31) - 1 if ans >= pow(2, 31) - 1 else pow(-2, 31))
        )

    while dividend >= divisor:
        dividend -= divisor

        ans += 1

    ans = ans * sign

    return min(pow(2, 31) - 1, max(pow(-2, 31), ans))


if __name__ == "__main__":
    dividend = -2147483648
    divisor = -1
    print(divideSmartWay(dividend, divisor))
