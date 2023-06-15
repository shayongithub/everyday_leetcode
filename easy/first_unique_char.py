def firstUniqChar(s: str) -> int:
    """
    Given a string s, find the first non-repeating character in it
        and return its index. If it does not exist, return -1.

    Approach:
        - Build a hash-map with the key is the character and the value is the index
            If we find that a key exists already, we can set it to some value in order to avoid it (like -1)
        - Filter out keys that appear more than once with value above
        - Return -1 if the filtered dictionary is empty
        - Return the minimum value from the dictionary

    """
    dic = {}

    for ind, char in enumerate(s):
        if char in dic:
            dic[char] = -1
        else:
            dic[char] = ind

    for i in range(len(s)):
        if dic[s[i]] == 1:
            return i
    
    return -1

    # filterd = dict((k, v) for k, v in dic.items() if v != -1)

    # if not filterd:
    #     return -1

    # return min(filterd.values())


if __name__ == "__main__":
    s = "leetcode"
    print(firstUniqChar(s))
