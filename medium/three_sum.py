from typing import List


def twoSum(nums: List[int], target: int) -> List[List[int]]:
    seen = {}
    res = []

    for i, value in enumerate(nums):
        remaining = target - value

        if remaining in seen:
            res.append([value, remaining])
        else:
            seen[value] = i

    return res


def threeSumWithHashmap(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []

    for i in range(
        len(nums) - 2
    ):  # As we lookin for three numbers and twoSum handle the left 2 elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = 0 - nums[i]

        two_sums = twoSum(nums[i + 1 :], target)

        if two_sums == []:
            continue
        else:
            for ls in two_sums:
                tmp = [nums[i]] + ls
                ans.append(tmp)

    output = []

    for i in ans:
        if i not in output:
            output.append(i)

    return output


def threeSumWith2Pointers(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        lt = i + 1
        rt = len(nums) - 1

        while lt < rt:
            two_sum = nums[lt] + nums[rt]

            if two_sum == -nums[i]:  # 0 - nums[i]
                ans.append([nums[i], nums[lt], nums[rt]])
                lt += 1

                # to prevent the case that the previous pointer is the same as current pointer
                #   each value can have exactly 1 element that add up to the target,
                #       so based on that, we can update just one pointer (either left or right)
                #         if we meet the duplicated pointer
                while nums[lt] == nums[lt - 1] and lt < rt:
                    lt += 1
            elif two_sum < -nums[i]:
                lt += 1
            else:
                rt -= 1

    return ans


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    # print(threeSumWithHashmap(nums))
    print(threeSumWith2Pointers(nums))
