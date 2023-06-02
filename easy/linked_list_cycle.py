from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:

    pos_dict = set()
    cur = head

    while cur is not None:
        
        if cur in pos_dict:
            return True
        else:
            pos_dict.add(cur)

        cur = cur.next
    
    return False