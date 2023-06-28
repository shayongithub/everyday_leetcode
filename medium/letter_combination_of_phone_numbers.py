from typing import List


def letterCombinations(digits: str) -> List[str]:
    if digits == "":
        return []

    import itertools

    ans = []

    hash_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    all_chars = list(map(lambda num: hash_map[num], digits))

    combinations = list(itertools.product(*all_chars))

    for comb in combinations:
        if comb is None:
            continue

        ans.append("".join(comb))

    return ans


if __name__ == "__main__":
    digits = "234"
    print(letterCombinations(digits))
