def titleToNumber(columnTitle: str) -> int:
    import string

    alphabet = list("0" + string.ascii_uppercase)

    def calCol(s):
        if len(s) == 1:
            return alphabet.index(s)
        if len(s) == 2:
            return 26 * alphabet.index(s[0]) + alphabet.index(s[-1])

        return 26 * calCol(s[:-1]) + alphabet.index(s[-1])

    return calCol(columnTitle)


def titleToNumberNoRecursion(columnTitle: str) -> int:
    import string

    alphabet = list("0" + string.ascii_uppercase)

    ans = 0

    for col in columnTitle:
        ans = ans * 26 + alphabet.index(col)

    return ans


def titleToNumberNoRecursion2(columnTitle: str) -> int:
    import string

    alphabet = list("0" + string.ascii_uppercase)

    ans = 0

    for i, col in enumerate(reversed(columnTitle)):
        ans = alphabet.index(col) * pow(26, i) + ans

    return ans


if __name__ == "__main__":
    columnTitle = "ZY"
    print(titleToNumberNoRecursion2(columnTitle))
