from typing import List


def plusOne(self, digits: List[int]) -> List[int]:
    """You are given a large integer represented as an integer array digits,
    where each digits[i] is the ith digit of the integer.
    The digits are ordered from most significant to least significant in left-to-right order.
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits."""
    extra = 0

    if digits[-1] == 9:
        extra = 1
        digits[-1] = 0

        for index in range(len(digits) - 2, -1, -1):
            if digits[index] + extra == 10:
                digits[index] = 0
                extra = 1
            else:
                digits[index] += 1
                extra = 0
                break

        if extra == 1:
            digits.insert(0, 1)
    else:
        digits[-1] += 1

    return digits


def plusOneLineCode(self, digits: List[int]) -> List[int]:
    return [int(i) for i in str(int("".join([str(digit) for digit in digits])) + 1)]
