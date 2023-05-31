def isPalindrome(s: str) -> bool:
    converted = ''.join(filter(str.isalnum, s)).lower().replace(' ', '')

    return converted[::] == converted[::-1]


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"

    print(isPalindrome(s))