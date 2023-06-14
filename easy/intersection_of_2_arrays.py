from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Given two integer arrays nums1 and nums2, return an array of their intersection.
        Each element in the result must appear as many times as it shows
            in both arrays and you may return the result in any order.


    Approach:
    - We can make use of the set object in python to find the intersection,
        the important thing to note that how many time each 'intersects' appear
    - We can use the Counter or count_dict to count how many times each 'intersects' occurs
    - Then find the intersection between the two keys of the counter and take the appearances of
        the smaller counter
    """
    from collections import Counter

    cnt1 = Counter(nums1)
    cnt2 = Counter(nums2)

    set1 = set(cnt1.keys())
    set2 = set(cnt2.keys())
    ans = []
    intersects = set1.intersection(set2)

    for num in intersects:
        if cnt1.get(num) >= cnt2.get(num):
            ans.extend([num] * cnt2.get(num))
        else:
            ans.extend([num] * cnt1.get(num))

    return ans
