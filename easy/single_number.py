from typing import List
from functools import reduce


def singleNumber(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n) as required additional space for sorted nums
    """
    if len(nums) == 1:
        return nums[0]

    sorted_nums = sorted(nums)

    i = 0

    while i < len(nums):
        if i == len(nums) - 1:
            return sorted_nums[i]

        if sorted_nums[i] != sorted_nums[i + 1]:
            return sorted_nums[i]
        else:
            i += 2


def singleNumberGood(nums: List[int]) -> int:
    '''
    Using bitwise operator - XOR to compare each number in the array.
    XOR return 0 if two numbers are the same, 1 otherwise

    The reduce() function accepts:
        - a function 
        - a sequence 
            Returns a single value calculated over the given sequence
            Details: https://thepythonguru.com/python-builtin-functions/reduce/
    '''

    return reduce(lambda x1, x2: x1 ^ x2, nums)


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print(singleNumber(nums))
    print(singleNumberGood(nums))
