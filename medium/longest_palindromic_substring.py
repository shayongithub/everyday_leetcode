def longestPalindrome(s: str) -> str:
    """
    Given a string s, return the longest palindromic substring in s.

    Approach:

    - The idea is check the palindrome from inside out
        e.g. with s = 'babad' we might check the
            first character b
                has no left char, right char is 'a' -> skip
            second character a
                has left char b == right char is 'b'
                    -> we keep expand it from inside out to check for larger palindrome
                        (e.g. aba and xabax is also palidrome)
        + The above idea work well for odd cases, with the even cases
            we need to adjust the left and right pointer

    - With each iteration, we check the left and right of the current char,
        and expand outward for each character
        + It takes n x n = O(n^2) time complexity
    """

    # Sub-functions to expand
    def get_palindrome(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]

    res = ""

    for i in range(len(s)):
        odd_palindrome = get_palindrome(s, i, i)

        # Increase the right pointer by 1 to check the even cases
        even_palindrome = get_palindrome(s, i, i + 1)

        # Compare between odd, even and resLen to update the longest string
        res = max([res, odd_palindrome, even_palindrome], key=len)

    return res


if __name__ == "__main__":
    s = "babad"
    print(longestPalindrome(s))
