from collections import Counter


def hammingWeight(n: int) -> int:
    binary = bin(n)[2:]

    counter = Counter(binary)
    return counter.get("1", 0)


if __name__ == "__main__":
    n = 0b00000010100101000001111010011100

    print(hammingWeight(n))
