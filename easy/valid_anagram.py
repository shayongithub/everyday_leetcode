def isAnagram(s: str, t: str) -> bool:
    """
    An Anagram is a word or phrase formed by rearranging the letters of a
        different word or phrase, typically using all the original letters exactly once.

    This problem does not include the meaning of the word so we can basically count the characters
        and return true if equal.

    Can do this with multiple ways: normal dict with conditional, defaultdict or just use Counter
    """
    if len(s) != len(t):
        return False

    from collections import Counter

    return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
