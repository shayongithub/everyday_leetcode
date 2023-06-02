def isPowerOfThree(n: int) -> bool:
    """
    Constraints; -2^31 <= n <= 2^31 - 1

    Obviously, n has to be greate than 0.
    As the contraints n <- 2^31 and by computation we know that
        3**19 is the largest number which is power of 3.
        So we can check that if n is a divisor of 3**19

    """
    return n > 0 and 3**19 % n == 0


def isPowerOfThreeRecursive(n: int) -> bool:
    """
    We recursively check that if the current n is divisible by 3.
        If it is, we continue to check n // 3.
            - Until we reach n = 1 that we will return True (3/3 = 1).
            As we use the operator "//", it will return the smallest integer even if it is not divisible by 3.
            Therefore, it will eventually return 0 (e.g. 7//3 = 2 -> 2//3 = 0)
            - So we will add another check n = 0 to determine that this number is not divisible by 3 and return False
        else just return False
    """
    if n == 1:
        return True

    if n == 0:
        return False

    return n % 3 == 0 and isPowerOfThreeRecursive(n // 3)


if __name__ == "__main__":
    n = 27
    print(isPowerOfThreeRecursive(n))
