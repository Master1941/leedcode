class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        return repr(self.val)


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> ListNode | None:
        a, b = headA, headB
        while a is not b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a


def create_linked_list(
        listA: list, listB: list, skipA: int, skipB: int
) -> list[ListNode]:
    """Генератор связных пересекающихся списков."""
    head_b = ListNode(listB[0])
    head_a = ListNode(listA[0])
    current_a = head_a
    current_b = head_b
    for i in range(1, skipA):
        current_a.next = ListNode(listA[i])
        current_a = current_a.next
    for i in range(1, skipB):
        current_b.next = ListNode(listB[i])
        current_b = current_b.next
    for i in range(skipB, len(listB)):
        current_a.next = current_b.next = ListNode(listB[i])
        current_a = current_b = current_b.next

    return head_a, head_b


if __name__ == "__main__":
    sol = Solution()

    intersectVal = 8
    listA = [4, 1, 4, 8, 4, 5]
    listB = [5, 6, 1, 4, 8, 4, 5]
    skipA = 2
    skipB = 3

    listA, listB = create_linked_list(listA, listB, skipA, skipB)

    # tail = ListNode(777, ListNode(88, ListNode(999)))
    # listA = ListNode(1, ListNode(2, ListNode(3, ListNode(4, tail))))
    # listB = ListNode(12, ListNode(22, ListNode(33, tail)))
    print(sol.getIntersectionNode(listA, listB,))
