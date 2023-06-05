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


if __name__ == "__main__":
    columnTitle = "A"
    print(titleToNumber(columnTitle))
