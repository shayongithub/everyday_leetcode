def reverseBits(n):
    n = bin(n)[2:]  # convert to binary, and remove the usual 0b prefix
    n = "%032s" % n  # print number into a pre-formatted string with space-padding
    n = n.replace(" ", "0")  # Convert the useful space-padding into zeros
    # Now we have a  proper binary representation, so we can make the final transformation
    return int(n[::-1], 2)


def reverseBitsManipulation(n: int) -> int:
    res = 0
    for _ in range(32):
        res = (res << 1) + (n & 1)
        n >>= 1
    return res


if __name__ == "__main__":
    n = 0b00000010100101000001111010011100

    print(reverseBitsManipulation(n))
