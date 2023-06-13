from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # simplist way
    # s[:] = s[::-1]

    # Using for loop
    # n = len(s)
    # for i in range(n // 2):
    #     s[i], s[n - i - 1] = s[n - i - 1], s[i]

    first = 0
    last = len(s) - 1

    while first <= len(s) // 2 and last >= len(s) // 2:
        s[first], s[last] = s[last], s[first]

        first += 1
        last -= 1


if __name__ == "__main__":
    s = [
        "A",
        " ",
        "m",
        "a",
        "n",
        ",",
        " ",
        "a",
        " ",
        "p",
        "l",
        "a",
        "n",
        ",",
        " ",
        "a",
        " ",
        "c",
        "a",
        "n",
        "a",
        "l",
        ":",
        " ",
        "P",
        "a",
        "n",
        "a",
        "m",
        "a",
    ]
    reverseString(s)
    print(s)
