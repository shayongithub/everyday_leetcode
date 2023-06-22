def reverse(x: int) -> int:
    """
    Given a signed 32-bit integer x, return x with its digits reversed.
        If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    """
    rev = int(str(abs(x))[::-1])
    max_int = pow(2, 31)
    min_int = -pow(2, 31)
    rev = -rev if x < 0 else rev

    return rev if rev < max_int and rev >= min_int else 0


def reverse_two(x: int) -> int:
    rev = int(str(abs(x))[::-1])

    return (rev if x > 0 else -rev) if rev.bit_length() < 32 else 0


if __name__ == "__main__":
    x = 120
    print(reverse(x))
