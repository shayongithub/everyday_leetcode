from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head.next is None:
        return None

    dummy_node = ListNode(0, next=head)

    left, right = dummy_node, head

    while right is not None:
        while n > 0 and right:
            right = right.next
            n -= 1

        if not right:
            break

        right = right.next
        left = left.next

    tmp = left.next
    left.next = tmp.next

    return dummy_node.next


if __name__ == "__main__":
    node5 = ListNode(5)
    node4 = ListNode(4, next=node5)
    node3 = ListNode(3, next=node4)
    node2 = ListNode(2, next=node3)
    node1 = ListNode(1, next=node2)

    # need to debug to see the list or create a function for that
    print(removeNthFromEnd(node1, 2))
