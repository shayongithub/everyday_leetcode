def isHappyStore(n: int) -> bool:
    """
    A happy number is a number defined by the following process:

    - Starting with any positive integer, replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does 
    not include 1.
    - Those numbers for which this process ends in 1 are happy.

    If the number is not happy, it will eventually lead to a number that already calculated.
    So we will create a set to store all the calculated numbers, and if it get calculated again. We will return false.
    Else if it meet 1, return True
    """
    seen = set()

    def sum_squared(n):
        rtn = 0

        while n > 0:
            rtn += (n % 10) ** 2

            n = n // 10

        return rtn

    while True:
        if sum_squared(n) == 1:
            return True
        else:
            if n in seen:
                return False

            seen.add(n)
            n = sum_squared(n)


def isHappyTwoPointers(n: int) -> bool:
    """
    Use the same ideas as above we can use the two pointers to detect whether there is a "loop",
    which just basically means 1 number get calculated twice (like detecting the loop inside linked list)
    """

    def sum_squared(n):
        rtn = 0

        while n > 0:
            rtn += (n % 10) ** 2

            n = n // 10

        return rtn

    slow = n
    fast = n

    while True:
        slow = sum_squared(slow)

        fast = sum_squared(sum_squared(fast))

        if slow != fast:
            continue
        else:
            break

    return slow == 1


if __name__ == "__main__":
    n = 19
    print(isHappyStore(n))
