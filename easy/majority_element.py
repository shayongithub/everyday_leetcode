from typing import List


def majorityElement(nums: List[int]) -> int:
    count_dict = {}

    for num in nums:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    return max(count_dict, key=lambda x: count_dict[x])


if __name__ == "__main__":
    nums = [3, 3, 4]

    print(majorityElement(nums))
