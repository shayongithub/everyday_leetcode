class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, new_node, position):
        """Insert a new node at the given position.
        Assume the first position is "1" and the last position is "-1".
        Inserting at position 3 means between the 2nd and 3rd elements."""

        current = self.head
        count = 1

        if position == 1:
            self.head = new_node
            new_node.next = current
        else:
            while current is not None:
                if position == count:
                    break

                prev = current
                current = current.next

                count += 1

            prev.next = new_node
            new_node.next = current

    def append(self, new_node):
        current = self.head
        if current:
            while current.next is not None:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = None

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.next


if __name__ == "__main__":
    e1 = Node(1)
    e2 = Node(2)
    e3 = Node(3)
    e4 = Node(4)
    e5 = Node(5)
    e6 = Node(6)
    e7 = Node(7)
    e8 = Node(8)

    linked_list = LinkedList(e1)

    linked_list.append(e2)
    linked_list.append(e3)

    print("Before Deleteing")
    linked_list.print_list()
    linked_list.delete(3)
    print("After Deleteing")
    linked_list.print_list()

    linked_list.append(e4)
    linked_list.append(e5)

    print("Before Inserting")
    linked_list.print_list()
    print("After Inserting")
    linked_list.insert(e6, 1)
    linked_list.insert(e7, 3)
    linked_list.insert(e8, 3)
    linked_list.print_list()
