from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    setA = set()
    curA = headA
    curB = headB

    while curA:
        setA.add(curA)

        curA = curA.next

    while curB:
        if curB in setA:
            return curB
        curB = curB.next

    return None


if __name__ == "__main__":
    