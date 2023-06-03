from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    ls = []
    cur = head

    while cur is not None:
        ls.append(str(cur.val))
        cur = cur.next

    string = "".join(ls)

    return string == string[::-1]
