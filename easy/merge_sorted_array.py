from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    last1 = m - 1
    last2 = n - 1

    write_ind = m + n - 1

    while last2 >= 0:
        if last1 >= 0 and nums1[last1] > nums2[last2]:
            nums1[write_ind] = nums1[last1]

            last1 -= 1
        else:
            nums1[write_ind] = nums2[last2]
            last2 -= 1

        write_ind -= 1


if __name__ == "__main__":
    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 5, 6]
    n = 5

    print(merge(nums1, m, nums2, n))
