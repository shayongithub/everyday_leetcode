from typing import List


def movezero_indes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    cnt = 0
    ls = []

    for num in nums:
        if num == 0:
            cnt += 1

    for _ in range(cnt):
        nums.remove(0)
        ls.append(0)

    nums.extend(ls)


def movezero_indesTwoPointer(nums: List[int]) -> None:
    """
    Keep track of 0
    Keep track of non-zero elements
        If the non_zero_ind meet a zero it will stop adding to the zero_ind (which help store the
            index of the current 0 element)
        then the next loop will switch between non_zero_ind and 0, which eventually
            push all the 0 to the end of the array
    """
    zero_ind = 0
    for non_zero_ind in range(len(nums)):
        if nums[non_zero_ind] != 0:
            nums[zero_ind], nums[non_zero_ind] = nums[non_zero_ind], nums[zero_ind]
            zero_ind += 1


if __name__ == "__main__":
    nums = [1, 2, 3, 0, 4, 0, 0, 5, 6]
    # movezero_indes(nums)
    movezero_indesTwoPointer(nums)
    print(nums)
