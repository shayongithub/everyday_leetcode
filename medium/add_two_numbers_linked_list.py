from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(head, num):
    if num != "":
        head.next = ListNode(num[0])
        create_linked_list(head.next, num[1:])


def addTwoNumbersNativezWay(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    You are given two non-empty linked lists representing two non-negative integers. T
        he digits are stored in reverse order, and each of their nodes contains a single digit.
            Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
    ind1 = 0
    ind2 = 0
    num1 = 0
    num2 = 0

    while l1:
        num1 += l1.val * pow(10, ind1)

        ind1 += 1
        l1 = l1.next

    while l2:
        num2 += l2.val * pow(10, ind2)

        ind2 += 1
        l2 = l2.next

    reverse = str(num1 + num2)[::-1]

    head = ListNode(int(reverse[0]))

    create_linked_list(head, reverse[1:])

    return head


if __name__ == "__main__":
    l1 = [2, 4, 3]  # 342
    l2 = [5, 6, 4]  # 465

    head1 = ListNode(2)
    head2 = ListNode(5)
    create_linked_list(head1, "43")
    create_linked_list(head2, "64")
    addTwoNumbersNativezWay(l1, l2)
