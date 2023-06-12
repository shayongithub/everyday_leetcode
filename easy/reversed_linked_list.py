from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    '''
    Using one temp node to hold the next element of the linked list.
        Then just use prev variable to hold the previous element for the current element
            to link to
    '''
    cur = head
    prev = cur
    tmp = ListNode()

    while cur:
        tmp.next = cur.next

        if cur is head:
            cur.next = None
        else:
            cur.next = prev

        prev = cur
        cur = tmp.next

    return prev


if __name__ == "__main__":
    node5 = ListNode(5)
    node4 = ListNode(4, next=node5)
    node3 = ListNode(3, next=node4)
    node2 = ListNode(2, next=node3)
    node1 = ListNode(1, next=node2)

    # need to debug to see the list or create a function for that
    print(reverseList(node1))
    
