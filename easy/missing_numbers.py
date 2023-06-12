from typing import List


def missingNumberSillyWay(nums: List[int]) -> int:
    """
    Given an array nums containing n distinct numbers in the range [0, n],
        return the only number in the range that is missing from the array.

    After sorting, the function checks for each pair of elements to see that the difference is greater than 1,
        then it means there is a missing number between them (as the range is from 0-n)

        Then we have 3 special conditions:
            - Length of nums is 1: the element is either 0 or 1 => return 1 - nums[0]
            - Our function can miss the head and tail of the range so we add another 2 condtions for that:
                + Check for the first element e.g. 0
                + Check for the last element e.g. n
    """
    n = len(nums)

    if n == 1:
        return n - nums[0]

    if n not in nums:
        return n

    if 0 not in nums:
        return 0

    sort = sorted(nums)

    first = 0
    second = 1

    while second < n:
        if sort[second] - sort[first] > 1:
            return sort[second] - 1

        first += 1
        second += 1


def missingNumberSum(nums: List[int]) -> int:
    """
    As only one element from the range is missing,
        we can calculate the sum of the range and subtract it from the actual sum of the inputs
            and fight the missing number

    Gauss's method comes in handy in this situation:
        sum(n) = (n*(n+1))/2
    """
    n = len(nums)
    sum_n = int((n * (n + 1)) / 2)

    actual_sum = sum(nums)

    return sum_n - actual_sum
    # return int((len(nums) * (len(nums) + 1)) / 2) - sum(nums)


if __name__ == "__main__":
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

    print(missingNumberSillyWay(nums))
    print(missingNumberSum(nums))
