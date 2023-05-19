from typing import List


def longestCommonPrefixMySillyWay(strs: List[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
    """
    if len(strs) == 1:
        return strs[0]

    prefix = ''
    first_word = strs[0]

    for ind in range(len(first_word)):
        not_match = False

        for word in strs[1:]:
            if not word.startswith(prefix + first_word[ind]):
                if prefix == '':
                    return ''
                not_match = True

        if not not_match:
            prefix += first_word[ind]
        else:
            break

    return prefix


def longestCommonPrefixSmarterWay(strs: List[str]) -> str:
    if len(strs) == 1:
        return strs[0]

    prefix = ''

    sorted_strs = sorted(strs)

    first = sorted_strs[0]
    last = sorted_strs[-1]

    for ind in range(min(len(first), len(last))):
        if first[ind] != last[ind]:
            break

        prefix += first[ind]

    return prefix


if __name__ == '__main__':
    strs = ["apcb", "apb"]

    longestCommonPrefixMySillyWay(strs)
