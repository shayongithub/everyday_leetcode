from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for index, cur_val in enumerate(nums):

        remaining = target - cur_val

        if remaining in seen:
            return [index, seen[remaining]]
        else:
            seen[cur_val] = index
