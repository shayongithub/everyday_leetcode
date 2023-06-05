from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    count_dict = {}

    for num in nums:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            return True

    return False


if __name__ == "__main__":
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(containsDuplicate(nums))
