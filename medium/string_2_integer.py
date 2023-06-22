def myAtoi(s: str) -> int:
    """
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

    The algorithm for myAtoi(string s) is as follows:

    1. Read in and ignore any leading whitespace.

    2. Check if the next character (if not already at the end of the string) is '-' or '+'.
        Read this character in if it is either.
            This determines if the final result is negative or positive respectively.
        Assume the result is positive if neither is present.

    3. Read in next the characters until the next non-digit character or the end of the input is reached.
        The rest of the string is ignored.

    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
        If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

    5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
        then clamp the integer so that it remains in the range.
        Specifically, integers < -2^31 should be clamped to -231, and integers > 2^31 - 1 should be clamped to 2^31 - 1.

    Return the integer as the final result.


    Note:
    - Only the space character ' ' is considered a whitespace character.
    - Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

    """
    ans = ""
    num = "0123456789"
    sign = 0
    s = s.lstrip()

    for i in s:
        if (i == "-" or i == "+") and sign == 0 and i == s[0]:
            sign = -1 if i == "-" else 1
            continue

        if i not in num:
            break

        ans += i

    if ans == "":
        return 0

    sign = sign if sign != 0 else 1

    ans = int(ans) * sign

    return (
        (pow(2, 31) - 1 if sign == 1 else -pow(2, 31))
        if ans.bit_length() >= 32
        else ans
    )


if __name__ == "__main__":
    s = "2147483648"
    print(myAtoi(s))
