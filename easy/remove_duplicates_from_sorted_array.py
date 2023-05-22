from typing import List


def removeDuplicatesTrick(nums: List[int]) -> int:
    nums[:] = sorted(set(nums))  # with [:] we can replaces element in place

    return len(nums)


def removeDuplicatesSillyWay(nums: List[int]) -> int:
    counter = {}

    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    for num, times in counter.items():
        while times != 1:
            nums.remove(num)
            times -= 1

    return len(nums)


def removeDuplicatesTwoPointer(nums: List[int]) -> int:
    insertIndex = 1

    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[insertIndex] = nums[i]

            insertIndex += 1

    return insertIndex


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    removeDuplicatesTwoPointer(nums)
