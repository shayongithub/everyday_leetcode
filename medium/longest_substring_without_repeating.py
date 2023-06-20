def lengthOfLongestSubstring(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.

    Approach:
    - Using sliding window with left and right pointers act as window boundaries
    - We have a dic with key is char and value is its index
        to keep track the appearance of characters and update the boundaries
    - We will iterate over the string with right pointers
    - We update the max_len if necessary

    - If the current character is not in the dic and
        if the corresponding index from the dic is smaller than the left pointer, which means:
            + This character has been seen before, but as its index is outside of the sliding window (< left),
                we can consider it as a 'unique' character of the current substring
    - If the current character is in the dic (repeating),
        then we update the left pointer to the next position after the last occurrence of the repeating character,
            in order word, we reset the substring to the next character of the first occurrence
                of the repeating character so we did not miss any new substring

    """
    ind_dic = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] not in ind_dic or ind_dic[s[right]] < left:
            ind_dic[s[right]] = right
            max_len = max(max_len, right - left + 1)
        else:
            left = ind_dic[s[right]] + 1
            ind_dic[s[right]] = right

    return max_len


if __name__ == "__main__":
    # s = "tmmzuxt"
    s = "dvdf"
    print(lengthOfLongestSubstring(s))
